import pyglet
from dialog import Dialog
from button import Button
from vbox import VBox
from hbox import HBox
from slider import Slider
from checkbox import Checkbox
from label import Label
from radiobutton import Radiobutton

# pyglet. create window
window = pyglet.window.Window(resizable=True)

# pywidget. put widgets in a container
vbox1 = VBox(elements=[Button()])
dialog1 = Dialog(title='My Dialog', x=100, y=100, content=vbox1, width=300, height=160)

vbox2 = VBox(elements=[Button()])
dialog2 = Dialog(title='My Dialog', x=150, y=150, content=vbox2, width=300, height=160)

# pywidget. put top widget(s) into pyglet 
window.push_handlers(dialog1)
window.push_handlers(dialog2)

# pywidget. event handlers for widgets
@window.event
def on_draw():
    window.clear()
    dialog1.on_draw()
    dialog2.on_draw()

# pyglet. event loop
pyglet.app.run()
