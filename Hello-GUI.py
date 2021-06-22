# hello-gui.py
# Import everything required from the tkinter module
from tkinter import *


# Function called by clicking my_button:
def change_text():
    my_label.config(text='Great, what about you?')

# Create the main tkinter window.
window = Tk()
window.title('My Application')

# Add an empty tkinter label widget and place it in a grid layout
my_label = Label(window, width=50, height=1, text="Hey, how's it going!")
my_label.grid(row=0, column=0)

# Add a tkinter button widget, place it in the grid layout
# add attach the change_text() function
my_button = Button(window, text='', width=30, command=change_text)
my_button.grid(row=1, column=0)
my_button.config(text='Please click the button for an answer')

# Enter the main event loop
window.mainloop()