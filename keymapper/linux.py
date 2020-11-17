#!/usr/bin/python3
# -*- coding: utf-8 -*-
# key-mapper - GUI for device specific keyboard mappings
# Copyright (C) 2020 sezanzeb <proxima@hip70890b.de>
#
# This file is part of key-mapper.
#
# key-mapper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# key-mapper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with key-mapper.  If not, see <https://www.gnu.org/licenses/>.


"""Device and evdev stuff that is independent from the display server."""


import subprocess
import multiprocessing
import threading
import asyncio

import evdev

from keymapper.logger import logger
from keymapper.mapping import custom_mapping, MAX_KEYCODE, MIN_KEYCODE


def can_grab(path):
    """Can input events from the device be read?

    Parameters
    ----------
    path : string
        Path in dev, for example '/dev/input/event7'
    """
    p = subprocess.run(['fuser', '-v', path])
    return p.returncode == 1


class KeycodeReader:
    """Keeps reading keycodes in the background for the UI to use.

    When a button was pressed, the newest keycode can be obtained from this
    object.
    """
    def __init__(self, device):
        self.device = device
        self.virtual_devices = []
        self.start_injecting()

    def clear(self):
        """Next time when reading don't return the previous keycode."""
        # read all of them to clear the buffer or whatever
        for virtual_device in self.virtual_devices:
            while virtual_device.read_one():
                pass

    def start_injecting_worker(self, path):
        """Inject keycodes for one of the virtual devices.

        This depends on a setxkbmap-loaded symbol file that contains
        the mappings for keycodes in the range of MIN and MAX_KEYCODE.
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        # TODO use uinput instead, then register somewhere its existance in
        #  order to setxkbmap it. Or give it a constant path that is known
        #  application wide
        device = evdev.InputDevice(path)
        uinput = evdev.UInput()

        for event in device.read_loop():
            if event.type != evdev.ecodes.EV_KEY:
                continue

            # this happens to report key codes that are 8 lower
            # than the ones reported by xev
            input_keycode = event.code + 8
            output_keycode = custom_mapping.get_keycode(input_keycode) - 8

            print(input_keycode, output_keycode)

            if output_keycode > MAX_KEYCODE or output_keycode < MIN_KEYCODE:
                continue

            # value: 1 for down, 0 for up, 2 for hold.
            device.write(evdev.ecodes.EV_KEY, output_keycode, event.value)
            device.write(evdev.ecodes.EV_SYN, evdev.ecodes.SYN_REPORT, 0)

    def start_injecting(self):
        """Read keycodes and inject the mapped character forever."""
        paths = _devices[self.device]['paths']

        logger.debug(
            'Starting injecting the mapping for %s on %s',
            self.device,
            ', '.join(paths)
        )

        # Watch over each one of the potentially multiple devices per hardware
        for path in paths:
            threading.Thread(
                target=self.start_injecting_worker,
                args=(path,)
            ).start()

    def read(self):
        """Get the newest key or None if none was pressed."""
        newest_keycode = None
        for virtual_device in self.virtual_devices:
            while True:
                event = virtual_device.read_one()
                if event is None:
                    break
                if event.type == evdev.ecodes.EV_KEY and event.value == 1:
                    # value: 1 for down, 0 for up, 2 for hold.
                    # this happens to report key codes that are 8 lower
                    # than the ones reported by xev
                    newest_keycode = event.code + 8
        return newest_keycode


_devices = None


class GetDevicesProcess(multiprocessing.Process):
    """Process to get the devices that can be worked with.

    Since InputDevice destructors take quite some time, do this
    asynchronously so that they can take as much time as they want without
    slowing down the initialization. To avoid evdevs asyncio stuff spamming
    errors, do this with multiprocessing and not multithreading.
    TODO to threading, make eventloop
    """
    def __init__(self, pipe):
        """Construct the process.

        Parameters
        ----------
        pipe : multiprocessing.Pipe
            used to communicate the result
        """
        self.pipe = pipe
        super().__init__()

    def run(self):
        """Do what get_devices describes."""
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

        # group them together by usb device because there could be stuff like
        # "Logitech USB Keyboard" and "Logitech USB Keyboard Consumer Control"
        grouped = {}
        for device in devices:
            # only keyboard devices
            # https://www.kernel.org/doc/html/latest/input/event-codes.html
            if evdev.ecodes.EV_KEY not in device.capabilities().keys():
                continue

            usb = device.phys.split('/')[0]
            if grouped.get(usb) is None:
                grouped[usb] = []
            grouped[usb].append((device.name, device.path))

        # now write down all the paths of that group
        result = {}
        for group in grouped.values():
            names = [entry[0] for entry in group]
            devs = [entry[1] for entry in group]
            shortest_name = sorted(names, key=len)[0]
            result[shortest_name] = {
                'paths': devs,
                'devices': names
            }

        self.pipe.send(result)


def get_devices():
    """Group devices and get relevant infos per group.

    Returns a list containing mappings of
    {group_name: {paths: [paths], devices: [names]} for input devices.

    For example, group_name could be "Logitech USB Keyboard", devices might
    contain "Logitech USB Keyboard System Control" and "Logitech USB Keyboard".
    paths is a list of files in /dev/input that belong to the devices.

    They are grouped by usb port.
    """
    global _devices
    if _devices is None:
        pipe = multiprocessing.Pipe()
        GetDevicesProcess(pipe[1]).start()
        # block until devices are available
        _devices = pipe[0].recv()
        logger.info('Found %s', ', '.join([f'"{name}"' for name in _devices]))
    return _devices
