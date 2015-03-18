#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Sample.
# using pywidget3 to make an exit button,
# but doing the remaining drawing from the application.

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

# pywidget. widget into pyglet
window.push_handlers(b1)

#
def MyDrawSpiral(scale):

    pyglet.gl.glColor4f(1.0, 1.0, 0, 1.0)
    glLineWidth(3)

    cx = 0.5*scale
    cy = 0.5*scale

    i = 0
    step = math.pi/20.0
    while i < math.pi*5:

        dx1 = math.sin(i) * i * 10
        dy1 = math.cos(i) * i * 10

        i += step

        dx2 = math.sin(i) * i * 10
        dy2 = math.cos(i) * i * 10


        line = [ (dx1+cx), (dy1+cy), (dx2+cx), (dy2+cy)]
        
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', line))


# pywidget. event handlers for widgets
@window.event
def on_draw():
    
    # app draw
    window.clear()

    w = window.width
    h = window.height
    scale = min(w,h)
    
    glLoadIdentity()
    glColor4f(1, 0.2, 0.2, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f( .2*scale, .2*scale)
    glVertex2f( .7*scale, .2*scale)
    glVertex2f( .8*scale, .8*scale)
    glEnd()

    #
    MyDrawSpiral(scale)

    # restore draw context for widgets
    glLoadIdentity()
    
    # pywidget draw
    b1.on_draw()

@b1.event
def on_button_press(button):
    print('Exit Clicked. Close window')
    window.close()

# pyglet. event loop
pyglet.app.run()
