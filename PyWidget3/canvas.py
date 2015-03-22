#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
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
from .shape import Rectangle, Ellipse, Cross, Star
from .widget import Widget

# ----------------------------------------------------------------------- HBox
class Canvas(Widget):
    ''' Canvas widget
    
    any empty widget, acts as a parent container for other widgets
    it handles mouse event and draw event routing.
    it handles relative move
    it does not handle relative scaling of children, if the window is resized
    '''
    # _________________________________________________________________ __init__
    def __init__(self, x=0, y=0, z=0, width=300, height=300,
                anchor_x='left', anchor_y='bottom', elements=[]):

      Widget.__init__(self,x,y,z,width,height,anchor_x,anchor_y)

      length = len(elements)
      for i in range(length):
        self._elements[i] = elements[i]
        self._elements[i].set_parent( self )

    # _________________________________________________________________ on_draw
    def on_draw(self):
 
        # save scissoring
        savescissor = (GLint * 4)()
        glGetIntegerv( GL_SCISSOR_BOX, savescissor)
        save_scissor_enable = glIsEnabled(GL_SCISSOR_TEST)

        # set scissoring
        glScissor( self._root_x, self._root_y,
                   self.width, self.height)
        glEnable(GL_SCISSOR_TEST)

        # draw self
        glTranslatef(self._root_x, self._root_y, self._root_z)
        self.dispatch_event('widget_draw', self)
        glTranslatef(-self._root_x, -self._root_y, -self._root_z)

        # restore scissoring
        glScissor( savescissor[0], savescissor[1],
                   savescissor[2], savescissor[3])
        
        if not save_scissor_enable:
            glDisable(GL_SCISSOR_TEST)
        
        # draw children
        Widget.on_draw(self)

Canvas.register_event_type('widget_draw')
