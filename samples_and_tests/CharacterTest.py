#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyglet
from pyglet.gl import *
from PyWidget3 import *
 
# pyglet window
window = pyglet.window.Window(resizable=True)

rowsize = 30
rowpixel = 200

# pywidget
label1 = Label( x=0, y=rowpixel,
                font_size=14,
                text='<font color=white>Character Info</font>',
              )
rowpixel -= rowsize

#
label2 = Label( x=0, y=rowpixel,
                font_size=11,
                text='<font color=white>Name</font>',
              )
ebox1 = EditBox( x=75, y=rowpixel, width=200, window=window)
rowpixel -= rowsize

#
label3 = Label( x=0, y=rowpixel,
                font_size=11,
                text='<font color=white>Subtext</font>',
              )
ebox2 = EditBox( x=75, y=rowpixel, window=window)
rowpixel -= rowsize

#
label4 = Label( x=0, y=rowpixel,
                font_size=11,
                text='<font color=white>Class</font>',
              )
class1 = Label(text="<font color=white>Fighter</font>", font_size=11)
class2 = Label(text="<font color=white>Wizard</font>", font_size=11)
class3 = Label(text="<font color=white>Healer</font>", font_size=11)
combo1 = ComboBox(x=75, y=rowpixel, width=200, elements=[class1, class2, class3])
rowpixel -= rowsize
 
#
desktop = Canvas(x=0, y=0, width=640, height=480,
                 elements=[label1, label2, ebox1, label3, ebox2, label4, combo1])

# pyglet event hander for pywidget
window.push_handlers(desktop)

#
@window.event
def on_draw():
    window.clear()
    desktop.on_draw()

pyglet.app.run()

