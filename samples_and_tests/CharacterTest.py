#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyglet
from pyglet.gl import *
from PyWidget3 import *
 
# pyglet window
window = pyglet.window.Window(resizable=True)

# pywidget
label_header = Label(font_size=14, text='<font color=white>Character Info</font>', text_anchor_x='center')

#
label_r1 = Label(font_size=11, text='<font color=white>Name</font>', anchor_x='left' )
ebox_r1 = EditBox(width=200, window=window)
ebox_r1.text = "Thud"
hbox_r1 = HBox( elements=[label_r1, ebox_r1] )

#
label_r2 = Label( font_size=11, text='<font color=white>Subtext</font>')
ebox_r2 = EditBox( width=200, window=window)
ebox_r2.text = "The barbarian"
hbox_r2 = HBox( elements = [ label_r2, ebox_r2] )

#
label_r3 = Label( font_size=11,text='<font color=white>Class</font>')
class1 = Label(text="<font color=white>Fighter</font>", font_size=11)
class2 = Label(text="<font color=white>Wizard</font>", font_size=11)
class3 = Label(text="<font color=white>Healer</font>", font_size=11)
combo_r3 = ComboBox(x=75, y=110, width=200, elements=[class1, class2, class3])
hbox_r3 = HBox(elements=[label_r3, combo_r3])

#
desktop = VBox(x=0, y=200, elements=[label_header, hbox_r1, hbox_r2, hbox_r3])

# pyglet event hander for pywidget
window.push_handlers(desktop)

#
@window.event
def on_draw():
    window.clear()
    desktop.on_draw()

pyglet.app.run()

