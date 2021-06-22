# DictionaryProject.py
from tkinter import *


# Function for click:
def click():
    entered_text = text_entry.get()  # get() function collects data from the required variable
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "Sorry there is no word like that. Please try again."
    output.insert(END, definition)


# Create the main tkinter window
window = Tk()
window.title('My Dictionary for Computer Science')
window.configure(background="black")


# Create a label
Label(window, text="Enter the word you would like a definition for:", bg="black", fg="white", font="none 12 bold")\
    .grid(row=1, column=0, sticky=W)

# Create a text entry box
text_entry = Entry(window, width=20, bg="white")
text_entry.grid(row=2, column=0, sticky=W)

# Add a submit button
Button(window, text="SUBMIT", width=6, command=click).grid(row=3, column=0, sticky=W)

# Create another label, for definitions
Label(window, text="\nDefinitions:", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky=W)

# Create a text box
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

# Enter the code for the words that will de defined.
my_compdictionary = {
    'algorithm': 'Step by step instructions to complete a task.',
    'bug': 'Piece of code that causes a program to fail.',
    'compiling': 'Assembling information collected from various sources.',
    'ASCII': 'Short for American Standard Code for Information Interexchange, '
             'ASCII is a standard that assigns letters, '
             'numbers, and other characters in the 256 slots available in the 8-bit code.',
    'hexadecimal': 'Alternatively referred to as Base 16 or hex, the hexadecimal numbering system uses combinations of '
                   '16 character digits to represent numbers. Hexadecimal uses all ten numbers in the decimal system '
                   '(0, 1, 2, 3, 4, 5, 6, 7, 8, and 9) and letters A through F. For example, "computer hope" in '
                   'hexadecimal becomes "636f6d707574657220686f7065".',
    'binary': 'Binary is a base 2 number system invented by Gottfried Leibniz that is made up of only two numbers: '
              '0 and 1. This number system is the basis for all binary code, which is used to write data such as the '
              'instructions that computer processors use, or the digital text you read every day.',
    'octal': 'Octal is a base-8 number system commonly used to represent binary numbers'
             ' and other numbers in a shorter form.',
    'decimal': 'Alternatively referred to as base 10, decimal is a numbering system comprised of the numerals '
              '0 to 9 that was first used by the Chinese in 1350 B.C..'
    }

# Exiting the program
Label(window, text="Click to exit:", bg="black", fg="white", font="none 12 bold")\
    .grid(row=6, column=0, sticky=W)


# Exit function
def close_window():
    window.destroy()
    exit()


# Exit Button
Button(window, text="Exit", width=14, command=close_window).grid(row=7, column=0, sticky=W)

# Enter the mainloop
window.mainloop()
