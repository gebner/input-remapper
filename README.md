# Key Mapper

**Almost done**

GUI tool to map input buttons to e.g. change the macro keys of a mouse or
any keyboard to something different. It should not be device specific, any
input device supported by Linux plug and play that reports keyboard events
will likely work.

This unfortunately doesn't apply to left/middle/right clicks of mice, or
the common back/forward thumb buttons, but the keypads of MMO mice seem to
work. Changing single keys of keyboards also works.

<p align="center">
    <img src="data/screenshot.png"/>
</p>

# Running

```bash
sudo python3 setup.py install && sudo key-mapper-gtk -d
```

You can also start it via your applications menu.

# Dependencies

`python-evdev`

# Tests

```bash
sudo python3 setup.py install && python3 tests/test.py
```

# Roadmap

- [x] show a dropdown to select an arbitrary device from `xinput list`
- [x] creating presets per device
- [x] renaming presets
- [x] show a list for mappings `[keycode -> target]`
- [x] read keycodes with evdev
- [x] make that list extend itself automatically
- [x] load that file with `setxkbmap` on button press
- [x] keep the system defaults for unmapped buttons
- [x] offer going back to the system default
- [x] highlight changes and alert before discarding unsaved changes
- [ ] automatically load the preset when the mouse connects
- [x] ask for administrator permissions using polkit
- [ ] make it work on wayland
- [ ] add to the AUR, provide .deb and .appimage files

This is incredibly overcomplicated due to various obstacles with xkb. If you
have questions about the code, feel free to open an issue. See HELP.md
