#!/usr/bin/python3
# -*- coding: utf-8 -*-
# input-remapper - GUI for device specific keyboard mappings
# Copyright (C) 2022 sezanzeb <proxima@sezanzeb.de>
#
# This file is part of input-remapper.
#
# input-remapper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# input-remapper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with input-remapper.  If not, see <https://www.gnu.org/licenses/>.

xmodmap = (
    b"keycode   8 =\nkeycode   9 = Escape NoSymbol Escape\nkeycode  10 = 1 exclam 1 exclam onesuperior exclamdown ones"
    b"uperior\nkeycode  11 = 2 quotedbl 2 quotedbl twosuperior oneeighth twosuperior\nkeycode  12 = 3 section 3 sectio"
    b"n threesuperior sterling threesuperior\nkeycode  13 = 4 dollar 4 dollar onequarter currency onequarter\nkeycode "
    b" 14 = 5 percent 5 percent onehalf threeeighths onehalf\nkeycode  15 = 6 ampersand 6 ampersand notsign fiveeighth"
    b"s notsign\nkeycode  16 = 7 slash 7 slash braceleft seveneighths braceleft\nkeycode  17 = 8 parenleft 8 parenleft"
    b" bracketleft trademark bracketleft\nkeycode  18 = 9 parenright 9 parenright bracketright plusminus bracketright"
    b"\nkeycode  19 = 0 equal 0 equal braceright degree braceright\nkeycode  20 = ssharp question ssharp question back"
    b"slash questiondown U1E9E\nkeycode  21 = dead_acute dead_grave dead_acute dead_grave dead_cedilla dead_ogonek dea"
    b"d_cedilla\nkeycode  22 = BackSpace BackSpace BackSpace BackSpace\nkeycode  23 = Tab ISO_Left_Tab Tab ISO_Left_Ta"
    b"b\nkeycode  24 = q Q q Q at Greek_OMEGA at\nkeycode  25 = w W w W lstroke Lstroke lstroke\nkeycode  26 = e E e E"
    b" EuroSign EuroSign EuroSign\nkeycode  27 = r R r R paragraph registered paragraph\nkeycode  28 = t T t T tslash "
    b"Tslash tslash\nkeycode  29 = z Z z Z leftarrow yen leftarrow\nkeycode  30 = u U u U downarrow uparrow downarrow"
    b"\nkeycode  31 = i I i I rightarrow idotless rightarrow\nkeycode  32 = o O o O oslash Oslash oslash\nkeycode  33 "
    b"= p P p P thorn THORN thorn\nkeycode  34 = udiaeresis Udiaeresis udiaeresis Udiaeresis dead_diaeresis dead_above"
    b"ring dead_diaeresis\nkeycode  35 = plus asterisk plus asterisk asciitilde macron asciitilde\nkeycode  36 = Retur"
    b"n NoSymbol Return\nkeycode  37 = Control_L NoSymbol Control_L\nkeycode  38 = a A a A ae AE ae\nkeycode  39 = s S"
    b" s S U017F U1E9E U017F\nkeycode  40 = d D d D eth ETH eth\nkeycode  41 = f F f F dstroke ordfeminine dstroke\nke"
    b"ycode  42 = g G g G eng ENG eng\nkeycode  43 = h H h H hstroke Hstroke hstroke\nkeycode  44 = j J j J dead_below"
    b"dot dead_abovedot dead_belowdot\nkeycode  45 = k K k K kra ampersand kra\nkeycode  46 = l L l L lstroke Lstroke "
    b"lstroke\nkeycode  47 = odiaeresis Odiaeresis odiaeresis Odiaeresis dead_doubleacute dead_belowdot dead_doubleacu"
    b"te\nkeycode  48 = adiaeresis Adiaeresis adiaeresis Adiaeresis dead_circumflex dead_caron dead_circumflex\nkeycod"
    b"e  49 = dead_circumflex degree dead_circumflex degree U2032 U2033 U2032\nkeycode  50 = Shift_L NoSymbol Shift_L"
    b"\nkeycode  51 = numbersign apostrophe numbersign apostrophe rightsinglequotemark dead_breve rightsinglequotemark"
    b"\nkeycode  52 = y Y y Y guillemotright U203A guillemotright\nkeycode  53 = x X x X guillemotleft U2039 guillemot"
    b"left\nkeycode  54 = c C c C cent copyright cent\nkeycode  55 = v V v V doublelowquotemark singlelowquotemark dou"
    b"blelowquotemark\nkeycode  56 = b B b B leftdoublequotemark leftsinglequotemark leftdoublequotemark\nkeycode  57 "
    b"= n N n N rightdoublequotemark rightsinglequotemark rightdoublequotemark\nkeycode  58 = m M m M mu masculine mu"
    b"\nkeycode  59 = comma semicolon comma semicolon periodcentered multiply periodcentered\nkeycode  60 = period col"
    b"on period colon U2026 division U2026\nkeycode  61 = minus underscore minus underscore endash emdash endash\nkeyc"
    b"ode  62 = Shift_R NoSymbol Shift_R\nkeycode  63 = KP_Multiply KP_Multiply KP_Multiply KP_Multiply KP_Multiply KP"
    b"_Multiply XF86ClearGrab\nkeycode  64 = Alt_L Meta_L Alt_L Meta_L\nkeycode  65 = space NoSymbol space\nkeycode  6"
    b"6 = Caps_Lock NoSymbol Caps_Lock\nkeycode  67 = F1 F1 F1 F1 F1 F1 XF86Switch_VT_1\nkeycode  68 = F2 F2 F2 F2 F2 "
    b"F2 XF86Switch_VT_2\nkeycode  69 = F3 F3 F3 F3 F3 F3 XF86Switch_VT_3\nkeycode  70 = F4 F4 F4 F4 F4 F4 XF86Switch_"
    b"VT_4\nkeycode  71 = F5 F5 F5 F5 F5 F5 XF86Switch_VT_5\nkeycode  72 = F6 F6 F6 F6 F6 F6 XF86Switch_VT_6\nkeycode "
    b" 73 = F7 F7 F7 F7 F7 F7 XF86Switch_VT_7\nkeycode  74 = F8 F8 F8 F8 F8 F8 XF86Switch_VT_8\nkeycode  75 = F9 F9 F9"
    b" F9 F9 F9 XF86Switch_VT_9\nkeycode  76 = F10 F10 F10 F10 F10 F10 XF86Switch_VT_10\nkeycode  77 = Num_Lock NoSymb"
    b"ol Num_Lock\nkeycode  78 = Scroll_Lock NoSymbol Scroll_Lock\nkeycode  79 = KP_Home KP_7 KP_Home KP_7\nkeycode  8"
    b"0 = KP_Up KP_8 KP_Up KP_8\nkeycode  81 = KP_Prior KP_9 KP_Prior KP_9\nkeycode  82 = KP_Subtract KP_Subtract KP_S"
    b"ubtract KP_Subtract KP_Subtract KP_Subtract XF86Prev_VMode\nkeycode  83 = KP_Left KP_4 KP_Left KP_4\nkeycode  84"
    b" = KP_Begin KP_5 KP_Begin KP_5\nkeycode  85 = KP_Right KP_6 KP_Right KP_6\nkeycode  86 = KP_Add KP_Add KP_Add KP"
    b"_Add KP_Add KP_Add XF86Next_VMode\nkeycode  87 = KP_End KP_1 KP_End KP_1\nkeycode  88 = KP_Down KP_2 KP_Down KP_"
    b"2\nkeycode  89 = KP_Next KP_3 KP_Next KP_3\nkeycode  90 = KP_Insert KP_0 KP_Insert KP_0\nkeycode  91 = KP_Delete"
    b" KP_Separator KP_Delete KP_Separator\nkeycode  92 = ISO_Level3_Shift NoSymbol ISO_Level3_Shift\nkeycode  93 =\nk"
    b"eycode  94 = less greater less greater bar dead_belowmacron bar\nkeycode  95 = F11 F11 F11 F11 F11 F11 XF86Switc"
    b"h_VT_11\nkeycode  96 = F12 F12 F12 F12 F12 F12 XF86Switch_VT_12\nkeycode  97 =\nkeycode  98 = Katakana NoSymbol "
    b"Katakana\nkeycode  99 = Hiragana NoSymbol Hiragana\nkeycode 100 = Henkan_Mode NoSymbol Henkan_Mode\nkeycode 101 "
    b"= Hiragana_Katakana NoSymbol Hiragana_Katakana\nkeycode 102 = Muhenkan NoSymbol Muhenkan\nkeycode 103 =\nkeycode"
    b" 104 = KP_Enter NoSymbol KP_Enter\nkeycode 105 = Control_R NoSymbol Control_R\nkeycode 106 = KP_Divide KP_Divide"
    b" KP_Divide KP_Divide KP_Divide KP_Divide XF86Ungrab\nkeycode 107 = Print Sys_Req Print Sys_Req\nkeycode 108 = IS"
    b"O_Level3_Shift NoSymbol ISO_Level3_Shift\nkeycode 109 = Linefeed NoSymbol Linefeed\nkeycode 110 = Home NoSymbol "
    b"Home\nkeycode 111 = Up NoSymbol Up\nkeycode 112 = Prior NoSymbol Prior\nkeycode 113 = Left NoSymbol Left\nkeycod"
    b"e 114 = Right NoSymbol Right\nkeycode 115 = End NoSymbol End\nkeycode 116 = Down NoSymbol Down\nkeycode 117 = Ne"
    b"xt NoSymbol Next\nkeycode 118 = Insert NoSymbol Insert\nkeycode 119 = Delete NoSymbol Delete\nkeycode 120 =\nkey"
    b"code 121 = XF86AudioMute NoSymbol XF86AudioMute\nkeycode 122 = XF86AudioLowerVolume NoSymbol XF86AudioLowerVolum"
    b"e\nkeycode 123 = XF86AudioRaiseVolume NoSymbol XF86AudioRaiseVolume\nkeycode 124 = XF86PowerOff NoSymbol XF86Pow"
    b"erOff\nkeycode 125 = KP_Equal NoSymbol KP_Equal\nkeycode 126 = plusminus NoSymbol plusminus\nkeycode 127 = Pause"
    b" Break Pause Break\nkeycode 128 = XF86LaunchA NoSymbol XF86LaunchA\nkeycode 129 = KP_Decimal KP_Decimal KP_Decim"
    b"al KP_Decimal\nkeycode 130 = Hangul NoSymbol Hangul\nkeycode 131 = Hangul_Hanja NoSymbol Hangul_Hanja\nkeycode 1"
    b"32 =\nkeycode 133 = Super_L NoSymbol Super_L\nkeycode 134 = Super_R NoSymbol Super_R\nkeycode 135 = Menu NoSymbo"
    b"l Menu\nkeycode 136 = Cancel NoSymbol Cancel\nkeycode 137 = Redo NoSymbol Redo\nkeycode 138 = SunProps NoSymbol "
    b"SunProps\nkeycode 139 = Undo NoSymbol Undo\nkeycode 140 = SunFront NoSymbol SunFront\nkeycode 141 = XF86Copy NoS"
    b"ymbol XF86Copy\nkeycode 142 = XF86Open NoSymbol XF86Open\nkeycode 143 = XF86Paste NoSymbol XF86Paste\nkeycode 14"
    b"4 = Find NoSymbol Find\nkeycode 145 = XF86Cut NoSymbol XF86Cut\nkeycode 146 = Help NoSymbol Help\nkeycode 147 = "
    b"XF86MenuKB NoSymbol XF86MenuKB\nkeycode 148 = XF86Calculator NoSymbol XF86Calculator\nkeycode 149 =\nkeycode 150"
    b" = XF86Sleep NoSymbol XF86Sleep\nkeycode 151 = XF86WakeUp NoSymbol XF86WakeUp\nkeycode 152 = XF86Explorer NoSymb"
    b"ol XF86Explorer\nkeycode 153 = XF86Send NoSymbol XF86Send\nkeycode 154 =\nkeycode 155 = XF86Xfer NoSymbol XF86Xf"
    b"er\nkeycode 156 = XF86Launch1 NoSymbol XF86Launch1\nkeycode 157 = XF86Launch2 NoSymbol XF86Launch2\nkeycode 158 "
    b"= XF86WWW NoSymbol XF86WWW\nkeycode 159 = XF86DOS NoSymbol XF86DOS\nkeycode 160 = XF86ScreenSaver NoSymbol XF86S"
    b"creenSaver\nkeycode 161 = XF86RotateWindows NoSymbol XF86RotateWindows\nkeycode 162 = XF86TaskPane NoSymbol XF86"
    b"TaskPane\nkeycode 163 = XF86Mail NoSymbol XF86Mail\nkeycode 164 = XF86Favorites NoSymbol XF86Favorites\nkeycode "
    b"165 = XF86MyComputer NoSymbol XF86MyComputer\nkeycode 166 = XF86Back NoSymbol XF86Back\nkeycode 167 = XF86Forwar"
    b"d NoSymbol XF86Forward\nkeycode 168 =\nkeycode 169 = XF86Eject NoSymbol XF86Eject\nkeycode 170 = XF86Eject XF86E"
    b"ject XF86Eject XF86Eject\nkeycode 171 = XF86AudioNext NoSymbol XF86AudioNext\nkeycode 172 = XF86AudioPlay XF86Au"
    b"dioPause XF86AudioPlay XF86AudioPause\nkeycode 173 = XF86AudioPrev NoSymbol XF86AudioPrev\nkeycode 174 = XF86Aud"
    b"ioStop XF86Eject XF86AudioStop XF86Eject\nkeycode 175 = XF86AudioRecord NoSymbol XF86AudioRecord\nkeycode 176 = "
    b"XF86AudioRewind NoSymbol XF86AudioRewind\nkeycode 177 = XF86Phone NoSymbol XF86Phone\nkeycode 178 =\nkeycode 179"
    b" = XF86Tools NoSymbol XF86Tools\nkeycode 180 = XF86HomePage NoSymbol XF86HomePage\nkeycode 181 = XF86Reload NoSy"
    b"mbol XF86Reload\nkeycode 182 = XF86Close NoSymbol XF86Close\nkeycode 183 =\nkeycode 184 =\nkeycode 185 = XF86Scr"
    b"ollUp NoSymbol XF86ScrollUp\nkeycode 186 = XF86ScrollDown NoSymbol XF86ScrollDown\nkeycode 187 = parenleft NoSym"
    b"bol parenleft\nkeycode 188 = parenright NoSymbol parenright\nkeycode 189 = XF86New NoSymbol XF86New\nkeycode 190"
    b" = Redo NoSymbol Redo\nkeycode 191 = XF86Tools NoSymbol XF86Tools\nkeycode 192 = XF86Launch5 NoSymbol XF86Launch"
    b"5\nkeycode 193 = XF86Launch6 NoSymbol XF86Launch6\nkeycode 194 = XF86Launch7 NoSymbol XF86Launch7\nkeycode 195 ="
    b" XF86Launch8 NoSymbol XF86Launch8\nkeycode 196 = XF86Launch9 NoSymbol XF86Launch9\nkeycode 197 =\nkeycode 198 = "
    b"XF86AudioMicMute NoSymbol XF86AudioMicMute\nkeycode 199 = XF86TouchpadToggle NoSymbol XF86TouchpadToggle\nkeycod"
    b"e 200 = XF86TouchpadOn NoSymbol XF86TouchpadOn\nkeycode 201 = XF86TouchpadOff NoSymbol XF86TouchpadOff\nkeycode "
    b"202 =\nkeycode 203 = Mode_switch NoSymbol Mode_switch\nkeycode 204 = NoSymbol Alt_L NoSymbol Alt_L\nkeycode 205 "
    b"= NoSymbol Meta_L NoSymbol Meta_L\nkeycode 206 = NoSymbol Super_L NoSymbol Super_L\nkeycode 207 = NoSymbol Hyper"
    b"_L NoSymbol Hyper_L\nkeycode 208 = XF86AudioPlay NoSymbol XF86AudioPlay\nkeycode 209 = XF86AudioPause NoSymbol X"
    b"F86AudioPause\nkeycode 210 = XF86Launch3 NoSymbol XF86Launch3\nkeycode 211 = XF86Launch4 NoSymbol XF86Launch4\nk"
    b"eycode 212 = XF86LaunchB NoSymbol XF86LaunchB\nkeycode 213 = XF86Suspend NoSymbol XF86Suspend\nkeycode 214 = XF8"
    b"6Close NoSymbol XF86Close\nkeycode 215 = XF86AudioPlay NoSymbol XF86AudioPlay\nkeycode 216 = XF86AudioForward No"
    b"Symbol XF86AudioForward\nkeycode 217 =\nkeycode 218 = Print NoSymbol Print\nkeycode 219 =\nkeycode 220 = XF86Web"
    b"Cam NoSymbol XF86WebCam\nkeycode 221 = XF86AudioPreset NoSymbol XF86AudioPreset\nkeycode 222 =\nkeycode 223 = XF"
    b"86Mail NoSymbol XF86Mail\nkeycode 224 = XF86Messenger NoSymbol XF86Messenger\nkeycode 225 = XF86Search NoSymbol "
    b"XF86Search\nkeycode 226 = XF86Go NoSymbol XF86Go\nkeycode 227 = XF86Finance NoSymbol XF86Finance\nkeycode 228 = "
    b"XF86Game NoSymbol XF86Game\nkeycode 229 = XF86Shop NoSymbol XF86Shop\nkeycode 230 =\nkeycode 231 = Cancel NoSymb"
    b"ol Cancel\nkeycode 232 = XF86MonBrightnessDown NoSymbol XF86MonBrightnessDown\nkeycode 233 = XF86MonBrightnessUp"
    b" NoSymbol XF86MonBrightnessUp\nkeycode 234 = XF86AudioMedia NoSymbol XF86AudioMedia\nkeycode 235 = XF86Display N"
    b"oSymbol XF86Display\nkeycode 236 = XF86KbdLightOnOff NoSymbol XF86KbdLightOnOff\nkeycode 237 = XF86KbdBrightness"
    b"Down NoSymbol XF86KbdBrightnessDown\nkeycode 238 = XF86KbdBrightnessUp NoSymbol XF86KbdBrightnessUp\nkeycode 239"
    b" = XF86Send NoSymbol XF86Send\nkeycode 240 = XF86Reply NoSymbol XF86Reply\nkeycode 241 = XF86MailForward NoSymbo"
    b"l XF86MailForward\nkeycode 242 = XF86Save NoSymbol XF86Save\nkeycode 243 = XF86Documents NoSymbol XF86Documents"
    b"\nkeycode 244 = XF86Battery NoSymbol XF86Battery\nkeycode 245 = XF86Bluetooth NoSymbol XF86Bluetooth\nkeycode 24"
    b"6 = XF86WLAN NoSymbol XF86WLAN\nkeycode 247 =\nkeycode 248 =\nkeycode 249 =\nkeycode 250 =\nkeycode 251 = XF86Mo"
    b"nBrightnessCycle NoSymbol XF86MonBrightnessCycle\nkeycode 252 =\nkeycode 253 =\nkeycode 254 = XF86WWAN NoSymbol "
    b"XF86WWAN\nkeycode 255 = XF86RFKill NoSymbol XF86RFKill\n"
)