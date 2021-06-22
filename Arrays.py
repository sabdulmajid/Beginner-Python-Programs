# Arrays.py
# Question 1:
from tkinter import *

fruit_list = ['Orange', 'Peach', 'Plum','Banana', 'Apple', 'Orange', 'Peach', 'Plum']
for i in fruit_list:
    print(i)
    if i == 'Apple':
        break

# Question 2:
x = []
enter_element = int(input("Enter the number of values you are going to enter: "))
for i in range(enter_element):
    enter_another_element = input('Enter the values to be entered into the array')
    x.append(enter_another_element)
    print(x)
print('This is your final array', x)

# Question 3:

# Question 4:
cletter=0
sletter=0
letter = str(input('Enter a word, in which the capital and small letters will be counted:  '))
for i in (letter):
    if ord(i) >= 65 and ord(i) <= 90:
        cletter = cletter+1
    else:
        sletter = sletter+1

print('capital letters=', cletter)

print('Small letters=', sletter)
