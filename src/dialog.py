#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Copyright (c) 2009 Nicolas Rougier, Matthieu Kluj, Jessy Cyganczuk
# Copyright (c) 2015 James Gaston
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions 
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# -----------------------------------------------------------------------------
import pyglet
from pyglet.gl import *
from shape import Rectangle, Ellipse, Cross, Star
from widget import Widget
from pyglet.event import EventDispatcher


# ----------------------------------------------------------------------- Dialog
class Dialog(Widget):
    ''' Dialog widget
    
    A dialog with a title, a close button and a content which has to be a children of Widget
    '''
    # _________________________________________________________________ __init__
    def __init__(self, x=0, y=0, z=0, width=300, height=300,
                 anchor_x='left', anchor_y='bottom', title='Dialog Title', content=None):

        Widget.__init__(self,x,y,z,width,height,anchor_x,anchor_y)

        fg = (0.5, 0.5, 0.5, 1)
        bg = (0.5, 0.6, 0.6, 1)
        fg2 = (1.0, 1.0, 1.0, 1)
        bg2 = (1.0, 0.0, 0.0, 1)
        
        frame = Rectangle (x=0, y=0, z=z,
                           width=width, height=height, radius=12,
                           foreground=fg, background=bg,
                           anchor_x=anchor_x, anchor_y=anchor_y)
        topbar = Rectangle (x=0, y=height-24, z=z,
                            width=width, height=24, radius=(0, 0, 12, 12),
                            foreground=fg, background=bg,
                            anchor_x=anchor_x, anchor_y=anchor_y)
        close_button = Cross (x=width-12, y=height-12, z=z+.1,
                              width=12, height=12,
                              branches=4,
                              foreground=fg2, background=bg2,
                              anchor_x='center', anchor_y='center')
        title = pyglet.text.Label(title,
                                  font_size=9, bold=True,
                                  color=(255,255,255,255),
                                  x=12, y=height-12,
                                  anchor_x='left', anchor_y='center')
        self._elements['frame'] = frame
        self._elements['topbar'] = topbar
        self._elements['tclose_button'] = close_button
        self._elements['title'] = title
        
        if not content is None:
          margin = 2
          content.height = height - topbar.height - 2 * margin;
          content.width = width - 2 * margin
          content.x = margin;
          content.y = margin;
          self._elements['acontent'] = content
          self._elements['acontent'].set_parent(self)
        
        self._is_dragging = False
        
    # __________________________________________________________ on_mouse_press
    def on_mouse_press(self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:

            # closse
            if self._elements['tclose_button'].hit_test(x - self.x, y - self.y):
              self._elements['tclose_button'].background = (0.8, 0.0, 0.0, 1)
              self._hidden = True
              return pyglet.event.EVENT_HANDLED

            # start drag
            elif self._elements['topbar'].hit_test(x - self.x, y - self.y):
              self._is_dragging = True
              self._elements['topbar'].background = (0.8, 0.8, 0.8, 0.5)

              self.set_topmost()
              return pyglet.event.EVENT_HANDLED
            
        # default - pass along to child widgets
        return super(Dialog, self).on_mouse_press(x, y, button, modifiers)
      
    # __________________________________________________________ on_mouse_release
    def on_mouse_release(self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
          self._is_dragging = False
          self._elements['topbar'].background = (0.5, 0.5, 0.5, 0.5)
        return super(Dialog, self).on_mouse_release(x, y, button, modifiers)
    
    # __________________________________________________________ on_mouse_drag    
    def on_mouse_drag(self, x, y, dx, dy, button,modifiers):
        if button == pyglet.window.mouse.LEFT:
            if self._is_dragging:
                self.x += dx
                self.y += dy
                return pyglet.event.EVENT_HANDLED
        return super(Dialog, self).on_mouse_drag(x, y, dx, dy, button, modifiers)

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    window = pyglet.window.Window(resizable=True)
    dialog = Dialog(x=50, y=50)
    window.push_handlers(dialog)
    
    @window.event
    def on_draw():
        window.clear()
        dialog.on_draw()

    pyglet.app.run()
