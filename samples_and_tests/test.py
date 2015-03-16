import pyglet
from PyWidget3 import *

# pyglet. create window
window = pyglet.window.Window(resizable=True)

# pywidget. create widgets
label1 = Label(text='<font face="Helvetica,Arial" size="2" color=white>First Label</font>',
               x=50, y=50)
label2 = Label(text='<font face="Helvetica,Arial" size="2" color=white>second Label</font>',
               x=50, y=50)
label3 = Label(text='<font face="Helvetica,Arial" size="2" color=white>third Label</font>',
                    x=50, y=50)
cbox = ComboBox(x=50, y=50, height=90, width=100,
                      elements=[label1, label2, label3])

button1 = Button(text='<font face="Helvetica,Arial" size="2" color="white">Click me 1</font>')
button2 = Button(text='<font face="Helvetica,Arial" size="2" color=white>Click me 2</font>')
button3 = Button(text='<font face="Helvetica,Arial" size="2" color=white>Click me 3</font>')
button4 = Button(text='<font face="Helvetica,Arial" size="2" color=white>Click me 4</font>')
checkbox = Checkbox()
label = Label(text='<font face="Helvetica,Arial" size="2" color=white>Some text</font>')
slider = Slider(x=50, y=50)

# pywidget. put widgets in a container
vbox = VBox(elements=[
            slider,
            HBox(elements=[button2, button3]),
            button1,
            cbox,
            HBox(elements=[checkbox, label, button4])])

# pywidget. put container in a dialog
dialog = Dialog(title='My Dialog', x=100, y=100, content=vbox, width=300, height=160)

# pywidget. put top widget(s) into pyglet 
window.push_handlers(dialog)

# pywidget. event handlers for widgets
@window.event
def on_draw():
    window.clear()
    dialog.on_draw()

@cbox.event
def on_comboboxbutton_press(cbox):
    print('change')

@slider.event
def on_value_change(slider):
    print('Value change : ', round(slider.value, 2))
    
@button1.event
def on_button_press(button):
    print('Button 1')

@button2.event
def on_button_press(button):
    print('Button 2')
    
@button3.event
def on_button_press(button):
    print('Button 3')
    
@button4.event
def on_button_press(button):
    print('Button 4')
    
@checkbox.event
def on_value_change(checkbox):
    print('Checkbox : ', checkbox.checked)

# pyglet. event loop
pyglet.app.run()
