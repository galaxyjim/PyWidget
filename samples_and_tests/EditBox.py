#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyglet
from pyglet.gl import *
from PyWidget3 import *

########################################
from PyWidget3.shape import Rectangle, Ellipse, Cross, Star
from PyWidget3.widget import Widget


# ----------------------------------------------------------------------- EditBox
class EditBox(Widget):
    ''' EditBox widget
    
    Simple text edit field
    '''

    # _________________________________________________________________ __init__
    def __init__(self, window, x=0, y=0, z=0, width=0, height=0, pad=(5,3),
                 font_size = 10, anchor_x='left', anchor_y='bottom',
                 text=''):

        fg = (.4,.4,.8, 1)
        fgint = (150, 150, 200, 255)
        bg = (.1,.1,.2, 1)
        xpad,ypad = pad

        #
        self.document = pyglet.text.document.UnformattedDocument(text)
        self.document.set_style(0, len(self.document.text), 
            dict(color=fgint)
        )

        font = self.document.get_font()
        fheight = font.ascent - font.descent

        layout = pyglet.text.layout.IncrementalTextLayout(
            self.document, width, fheight, multiline=False)
        
        self.caret = pyglet.text.caret.Caret(layout, color=(255,255,255))
        self.on_unset_focus()
        #
        if width == 0 and len(text) > 0:
            width = layout.content_width + 2 * xpad
        elif width == 0:
            width = 200
            
        if height == 0:
            height = layout.content_height + 2 * ypad

        #
        layout.x = xpad
        layout.y = ypad
        layout.height = height - 2*ypad
        layout.width = width - 2*xpad

        frame = Rectangle( x=0, y=0, z=z,
                           width=width, height=height, radius=0,
                           foreground=fg, background=bg,
                           anchor_x=anchor_x, anchor_y=anchor_y)
        
        self.text_cursor = window.get_system_mouse_cursor('text')

        #
        Widget.__init__( self, x, y, z, width, height, anchor_x, anchor_y)        

        self._elements['frame'] = frame
        self._elements['layout'] = layout

    #
    def on_mouse_press(self, x, y, button, modifiers):
        if self.hit_test(x,y):
            self.set_focus(self)
            self.caret.on_mouse_press(x-self._root_x, y-self._root_y, button, modifiers)
            return pyglet.event.EVENT_HANDLED
        
        if self.caret.visible:
            self.set_focus(None)
            
        return pyglet.event.EVENT_UNHANDLED


    #
    def on_text(self, text):
        self.caret.on_text(text)

    #
    def on_text_motion(self, motion):
        self.caret.on_text_motion(motion)
      
    #
    def on_text_motion_select(self, motion):
        self.caret.on_text_motion_select(motion)

    #
    def on_unset_focus(self):
        self.caret.visible = False
        self.caret.mark = 0
        self.caret.position = 0

    #
    def on_set_focus(self):
        self.caret.visible = True
        self.caret.mark = 0
        self.caret.position = len(self._elements['layout'].document.text)
 
# pyglet window
window = pyglet.window.Window(resizable=True)

# pywidget
ebox1 = EditBox(text='Text Here. abcdefghijklmnopqrstuvwxyzWTLM',
                x=50, y=75, window=window)
ebox2 = EditBox(text='second line',
                x=50, y=175, window=window)
button = Button(text="BBBB", x=50, y=125)
desktop = Canvas(x=0, y=0, width=640, height=480, elements=[ebox1, button, ebox2])

# pyglet event hander for pywidget
window.push_handlers(desktop)

#
@window.event
def on_draw():
    window.clear()
    desktop.on_draw()

#
pyglet.app.run()

