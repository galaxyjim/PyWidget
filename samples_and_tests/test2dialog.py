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
from PyWidget3 import *

# pyglet. create window
window = pyglet.window.Window(resizable=True)

# pywidget. put widgets in a container
b1 = Button(text="B1")
vbox1 = VBox(elements=[b1])
dialog1 = Dialog(title='My Dialog', x=100, y=50, content=vbox1, width=300, height=160)

b2 = Button(text="B2")
vbox2 = VBox(elements=[b2])
dialog2 = Dialog(title='My Dialog', x=150, y=220, content=vbox2, width=300, height=160)

main_gui_window = Canvas(elements=[dialog1, dialog2])

# pywidget. put top widget into pyglet. you should only have one top level widget per opengl window.
window.push_handlers(main_gui_window)

# pywidget. event handlers for widgets
@window.event
def on_draw():
    window.clear()
    main_gui_window.on_draw()

@b1.event
def on_button_press(button):
    print('Click 1')

@b2.event
def on_button_press(button):
    print('Click 2')
 
# pyglet. event loop
pyglet.app.run()
