#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Sample.
# using pywidget3 to make an exit button,
# but doing the remaining drawing from the application.
#
# in contrast to test3, this draw is done during a callback.

import pyglet
from pyglet.gl import *
from PyWidget3 import *
import math # used for demo draw

# pyglet. create window
config = pyglet.gl.Config(alpha_size=8,
                          sample_buffers=1,
                          samples=8,    # tell pyglet to antialias in opengl
                          double_buffer=True,
                          depth_size=24,
                          stencil_size=8)

window = pyglet.window.Window(config=config)

# pywidget. put widgets in a container
b1 = Button(text="EXIT", x=20, y=20)
drawarea = Canvas(x=100, y=200, width=100, height=100)
label = Label(x=100, y=350, text='<font color=white size="4">OpenGL draw during <i>widget</i> callback</font>')
desktop = Canvas(x=0, y=0,
                 width=window.width, height=window.height,
                 elements=[b1, label, drawarea]) 

# pywidget. widget into pyglet
window.push_handlers(desktop)

# pywidget. canvas allows user drawing.
# Note: widget_draw event doesn't have setup clipping,
#       it only prepares the x/y offset of the draw area.
@drawarea.event
def widget_draw(canvas):

    pyglet.gl.glColor4f(0.8, 0.0, 0.2, 1.0)
    glLineWidth(3)

    cx = canvas.width/2
    cy = canvas.height/2

    # draw frame, just for visual reference
    # could have been done by adding a pywidget rectangle
    # but we are showing off using opengl inside a widget
    line = [0, 0, 0, canvas.height]
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', line))
    line = [0, canvas.height, canvas.width, canvas.height]
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', line))
    line = [canvas.width, canvas.height, canvas.width, 0]
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', line))
    line = [canvas.width, 0, 0, 0]
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', line))

    # draw a spiral. just to show off
    pyglet.gl.glColor4f(1.0, 1.0, 0.0, 1.0)
    i = 0
    step = math.pi/20.0
    while i < math.pi*10:

        dx1 = math.sin(i) * i
        dy1 = math.cos(i) * i

        i += step

        dx2 = math.sin(i) * i
        dy2 = math.cos(i) * i

        line = [ (dx1+cx), (dy1+cy), (dx2+cx), (dy2+cy)]
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', line))

# pywidget. draw widgets
@window.event
def on_draw():
    
    # app draw
    window.clear()

    # restore draw context for widgets
    glLoadIdentity()
    
    # pywidget draw
    desktop.on_draw()

# pywidget. button press
@b1.event
def on_button_press(button):
    print('Exit Clicked. Close window')
    window.close()

# pyglet. event loop
pyglet.app.run()
