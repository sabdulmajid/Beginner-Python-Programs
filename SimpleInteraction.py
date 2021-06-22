# SimpleInteraction.py
print("Hello, I'm Python!")

# Input, assignment
name = str(input('What is your name?\n'))
print('Hi, %s, how old are you?' % name)
Age = (int(input("")))
print('That is awesome! Which grade are you in?')
Grade = (int(input("")))
Boundary = Grade + 5


# The conditions.
if Boundary > Age:
    print('That\'s young for your age!')
elif Boundary == Age:
    print('That\'s perfect for your age!')
else:
    print('You\'re old for your grade!')

print('''\
Menu:
1- Young
2- Old
3- None of the above
''')  # The '\'  gets rid of the space.

print("The sum of 1 + 2 = {0}".format(1+2))

s = 'supercalifragilisticexpialidocious'
print('The amount of letters in the word "supercalifragilisticexpialidocious" is %s, '
      'which is the longest word in the English dictionary.' % len(s))

square_numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
square_numbers.append(11**2)
print(square_numbers)
square_numbers.append(12**2)
print(square_numbers)
square_numbers.append(13**2)
print(square_numbers)
square_numbers.append(14**2)
print(square_numbers)
square_numbers.append(15**2)
print(square_numbers)
print(square_numbers[13:])
print(square_numbers[8])
