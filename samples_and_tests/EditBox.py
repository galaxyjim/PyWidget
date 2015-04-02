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

    #
    def _get_text(self):
        return self.document.text

    def _set_text(self, text):
        self.document.text = text

    text = property(_get_text, _set_text,
        doc='''text data displayed by the widget

        :type: string
        ''')

 
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

