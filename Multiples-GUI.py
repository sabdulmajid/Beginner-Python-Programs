# Multiples-GUI.py

from tkinter import *


def multiply():
    # get contents of textbox_input
    number = int(textbox_input.get())
    # clear output text box
    textbox_output.delete(0.0, END)
    # process and output result
    for counter in range(1, 13):
        multiple = str(number * counter) + '\n'
        textbox_output.insert(END, multiple)


# Build the GUI.
window = Tk()
window.title("Shaikh's Multiple App")

# Give the window it's dimensions.
window.geometry('150x350')
window.configure(background='beige')

# Create the labels.
input_label = Label(window, text='Number: ', bg='beige')
input_label.grid(row=0, column=0)
output_label = Label(window, text='\nOutput: ', bg='beige')
output_label.grid(row=2, column=0)

# Create text-entry box for entering the number
textbox_input = Entry(window, width=5)
textbox_input.grid(row=1, column=0)

# Create text box for outputting multiples.
textbox_output = Text(window, height=15, width=6)
textbox_output.grid(row=3, column=0)

# Create the button
multiply_button = Button(window, text='Multiply', command=multiply)
multiply_button.grid(row=1, column=1)

window.mainloop()
