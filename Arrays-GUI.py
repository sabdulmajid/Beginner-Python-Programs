# Arrays-GUI.py
from tkinter import *

# Declare the  global variable to allow all subroutines to use it:
task = [None] * 4

# Define all functions:


def input_data():
    # Collect values from Entry Boxes:
    data_item = int(textbox1.get())
    index = int(textbox2.get())
    # Insert new value into array
    task[index] = data_item


def output_data():
    # Collect the index from the user:
    index = int(textbox3.get())
    # Clear output textbox and display data
    textbox4.delete(0, END)
    textbox4.insert(END, task[index])


# Build the GUI part of the program
# Padding is added to some widgets:
window = Tk()
window.title("Shaikh's Array Application")
bg_colour = 'linen'

# Create the input and output frames
input_frame = Frame(window, bg=bg_colour)
input_frame.grid(row=0, column=0, ipadx=5, ipady=5)
output_frame = Frame(window, bg=bg_colour)
output_frame.grid(row=0, column=1, ipadx=5, ipady=5)

# Create the labels
input_label1 = Label(input_frame, text='Data Item to Add:', bg=bg_colour)
input_label1.grid(row=1, column=0, sticky=W)
input_label2 = Label(input_frame, text='Index to be Used:', bg=bg_colour)
input_label2.grid(row=2, column=0, sticky=W)
output_label1 = Label(output_frame, text='Index to Display:', bg=bg_colour)
output_label1.grid(row=1, column=0, sticky=W)
output_label2 = Label(output_frame, text='Value of Index:', bg=bg_colour)
output_label2.grid(row=2, column=0, sticky=W)

# Create the buttons
inputButton = Button(input_frame, text='Input', command=input_data, width=24)
inputButton.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
outputButton = Button(output_frame, text='Output', command=output_data, width=24)
outputButton.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

# Create the textbox(s):
textbox1 = Entry(input_frame, width=10)
textbox1.grid(row=1, column=1)
textbox2 = Entry(input_frame, width=10)
textbox2.grid(row=2, column=1)
textbox3 = Entry(output_frame, width=10)
textbox3.grid(row=1, column=1)
textbox4 = Entry(output_frame, width=10)
textbox4.grid(row=2, column=1)

# start tkinter loop
window.mainloop()
