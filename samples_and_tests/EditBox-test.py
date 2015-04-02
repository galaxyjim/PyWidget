#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyglet
from pyglet.gl import *
from PyWidget3 import *
 
# pyglet window
window = pyglet.window.Window(resizable=True)

# pywidget
label1 = Label( text="<font color=white>1</font>", x=0, y=75, width=50)
ebox1 = EditBox(text='bottom line',
                x=50, y=75, width=200, window=window)
label2 = Label( text="<font color=white>2</font>", x=0, y=175, width=50)
ebox2 = EditBox(text='top line',
                x=50, y=175, width=200, window=window)
button = Button(text="<font color=white>Copy 1 to 2</font>", x=50, y=125)
desktop = Canvas(x=0, y=0, width=640, height=480, elements=[label1, ebox1, label2, button, ebox2])

# pyglet event hander for pywidget
window.push_handlers(desktop)

#
@window.event
def on_draw():
    window.clear()
    desktop.on_draw()

@button.event
def on_button_press(button):
    print(ebox1.text)
    ebox2.text = ebox1.text
    
pyglet.app.run()

