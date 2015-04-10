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
from .shape import Rectangle, Ellipse, Cross, Star
from .widget import Widget


# ----------------------------------------------------------------------- VBox
class VBox(Widget):
    ''' Slider widget
    
    Used to split content into vertical parts
    '''
    # ____________________________________________________________________ __init__
    def __init__(self, x=0, y=0, z=0, width=0, height=0,
                anchor_x='left', anchor_y='bottom', elements=[]):

      self.margin = 3
      save_height = False

      if width == 0:
          width = max( [thing.width for thing in elements] ) + 2 * self.margin

      if height == 0:
          height = sum( [thing.height for thing in elements] ) + (len(elements)+1) * self.margin
          save_height = True

      Widget.__init__(self,x,y,z,width,height,anchor_x,anchor_y)

      length = len(elements)
      first = True
      for i in reversed(range(length)):
        if not save_height:
            elements[i].height = height / length - 2 * self.margin
        elements[i].width = width - 2 * self.margin
        elements[i].x = self.margin
        if first:
            first = False
            elements[i].y = self.margin
        else:
            elements[i].y = elements[i+1].y + elements[i+1].height + self.margin
                    
        self._elements[i] = elements[i]
        self._elements[i].set_parent( self )
      
    # ____________________________________________________________________ update_width
    def update_width(self):
      for i in range(len(self._elements)):
        self._elements[i].width = self.width - 2 * self.margin

    # ____________________________________________________________________ update_height
    def update_height(self):
      length = len(self._elements)
      first = True
      for i in reversed(range(length)):
        self._elements[i].height = self.height / length - self.margin
        if first:
            first = False
            self._elements[i].y = self.margin
        else:
            self._elements[i].y = self._elements[i+1].y + self._elements[i+1].height + self.margin
