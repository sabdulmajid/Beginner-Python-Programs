# Multiples-CL.py

# Question 1:
# With FOR Loop:
number = int(input('Enter a number, for which the first ten multiples of the number:  '))
for counter in range(1, 11):
    multiple = counter * number
    print(number,'x', counter,'=', multiple)



# With WHILE Loop:
number  = int(input('Enter a number, for which the first ten multiples will be shown:  '))
counter = 0
while counter < 10:
    counter = counter + 1
    multiple = counter * number
    print(number, 'x', counter, '=', multiple)



# Question 2:
# With FOR Loop:
totalpass = 0
totalfail = 0
invalid = 0
for counter in range(1, 11):
    number = int(input('\nEnter the mark of a student '))
    if 100 >= number >= 50:
        totalpass = totalpass + 1
        print('You PASSED')
    elif 50 > number >= 0:
        totalfail = totalfail + 1
        print('You FAILED')
    else:
        invalid = invalid + 1
        print('The mark you have entered is invalid')
print('\nThe total passes were:', totalpass)
print('The total fails were:', totalfail)
print('The total invalid inputs were:', invalid)


# With WHILE Loop:
counter = 0
totalpass = 0
totalfail = 0
invalid = 0
while counter < 10:
    counter = counter + 1
    number = int(input('\nEnter the mark of a student '))
    if 100 >= number >= 50:
        totalpass = totalpass + 1
        print('You PASSED')
    elif 50 > number >= 0:
        totalfail = totalfail + 1
        print('You FAILED')
    else:
        invalid = invalid + 1
        print('The mark you have entered is invalid')
print('The total passes were:', totalpass)
print('The total fails were:', totalfail)
print('The total invalid inputs were:', invalid)
