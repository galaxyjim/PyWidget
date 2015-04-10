#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Copyright (c) 2015 James Gaston
# Copyright (c) 2009 Nicolas Rougier, Matthieu Kluj, Jessy Cyganczuk
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
from .shape import Rectangle, Ellipse, Cross, Star
from .widget import Widget
from .label import Label

# ----------------------------------------------------------------------- Button
class ComboBox(Widget):
    ''' ComboBox widget

    This is a basic ComboBox Button.
    '''
    # _________________________________________________________________ __init__
    def __init__(self, x=0, y=0, z=0,
                 width=0, height=0,
                 anchor_x='left',
                 anchor_y='bottom',
                 elements=[]):


        #
        if height == 0:
            height = max( [thing.height for thing in elements] )
        if width == 0:
            width = max( [thing.width for thing in elements] )

        Widget.__init__(self,x,y,z,width,height,anchor_x,anchor_y)

        fg = (.5,.5,.5, 1)
        bg = (.5,.5,.5,.5)

        self.margin = 3
        self.ropen = 0

        # 
        length = len(elements)

        #
        chooselabel = Label(text = '<font color=white>...</font>',
                            x = self.margin,
                            y = self.margin,
                            z = z,
                            font_size=11,
                            height = height - 2*self.margin,
                            width = width - 2*self.margin)

        frame = Rectangle (x = 0,
                           y = height,
                           z = z,
                           width=width, height=-height, radius=0,
                           foreground=fg, background=bg,
                           anchor_x=anchor_x, anchor_y=anchor_y)

        self._elements['frame'] = frame
        self._elements['chooselabel'] = chooselabel

        #
        for i in range(length):
            elements[i].height = height - 2*self.margin
            elements[i].width = width - 2*self.margin
            elements[i].x = self.margin
            elements[i].y = self.margin - (i+1)*(height - self.margin)
            self._elements[i] = elements[i]
            self._elements[i]._hidden = True

    # ____________________________________________________________________ update_width
    def update_width(self):

        for i in range(len(self._elements) - 2):
            self._elements[i].width = self.width - 2 * self.margin
            self._elements[i].x = self.margin

        self._elements['chooselabel'].x = self.margin
        self._elements['chooselabel'].width = self.width - 2 * self.margin

        self._elements['frame'].x = 0
        self._elements['frame'].width = self.width

    # ____________________________________________________________________ update_height
    def update_height(self):
        
        length = len(self._elements) - 2
        for i in range(length):
            self._elements[i].height = self.height - 2 * self.margin
            self._elements[i].y = self.margin - (i+1)*(self.height + self.margin)

        self._elements['chooselabel'].y = self.margin
 
        self._elements['frame'].y = self.height
        self._elements['frame'].height = -self.height
 
    # ____________________________________________________________________ on_mouse_press
    def on_mouse_press(self, x, y, ComboboxButton, modifiers):
        if ComboboxButton == pyglet.window.mouse.LEFT:

            # opening
            if self._elements['chooselabel'].hit_test(x - self.x, y - self.y) and self.ropen == 0:
                
                self._elements['frame'].background = (0.8, 0.8, 0.8, 0.5)
                self._elements['frame'].height = - self._elements['chooselabel'].height


                minv = 0
                for i in range(len(self._elements) - 2):
                    self._elements[i]._hidden = False
                    minv = min( minv, self._elements[i].y )

                self._elements['frame'].height = -(self.height - minv + self.margin)

                self.ropen = 1

                return pyglet.event.EVENT_HANDLED

            # closing
            if self.ropen == 1:
                
                for i in range(len(self._elements) - 2):
                    if self._elements[i].hit_test(x - self.x, y - self.y):

                        self._elements['chooselabel'].set_text(self._elements[i].text)

                        self.dispatch_event('on_comboboxbutton_press', self)

                        self._elements['frame'].background = (0.8, 0.8, 0.8, 0.5)
                        self._elements['frame'].height = -self.height

                        for i in range(len(self._elements) - 2):
                            self._elements[i]._hidden = True

                        self.ropen = 0
                        return pyglet.event.EVENT_HANDLED

        return pyglet.event.EVENT_UNHANDLED

    # ___________________________________________________________ on_mouse_release
    def on_mouse_release(self, x, y, ComboboxButton, modifiers):
        if ComboboxButton == pyglet.window.mouse.LEFT:
          if self.ropen == 0:
              # closed. looks like a button
              self._elements['frame'].background = (0.5, 0.5, 0.5, 0.5)
          else:
              # open. looks like a list box
              self._elements['frame'].background = (0.3, 0.4, 0.5, 0.95)
          self.set_topmost()
        return pyglet.event.EVENT_UNHANDLED

ComboBox.register_event_type('on_comboboxbutton_press')
