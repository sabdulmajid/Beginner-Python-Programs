# gender-gui.py
from tkinter import *


# Functions go here:
def change_text():
    my_label.config(text=gender.get())


# GUI code goes here:
# Create the main tkinter window
window = Tk()
window.title('My Application')

# Add an empty tkinter label widget and place it in a grid layout.
my_label = Label(window, width=50, height=1, text='')
my_label.grid(row=0, column=0)

# Create a tkinter string variable object for the radio buttons
gender = StringVar()

# Add a tkinter button widget. place it in a grid layout
# and attach the change_text() function
my_button = Button(window, text='Submit', width=10, command=change_text())
my_button.grid(row=1, column=0)


# Add two radio button widgets
# Use optional sticky argument to align left
radio1 = Radiobutton(window, text='Female', variable=gender, value='female')
radio1.grid(row=2, column=0, sticky=W)
radio1.select()  # pre-selects this radio button for the user
radio2 = Radiobutton(window, text='Male', variable=gender, value='male')
radio2.grid(row=3, column=0, sticky=W)

# Enter the main loop event
window.mainloop()



