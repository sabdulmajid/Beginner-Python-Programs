# Tasks - Loops.py

# Question 1:
print('Question 1:')
number = int(input('Enter a number to be factorial-ed   '))
i = number
for i in range(1, number):
    number = number * i
    i = i - 1
print('The factorial is', number)

# Question 2:
print('\nQuestion 2:')
print('The numbers between 1 and 20 which are divisible by 2 are: ')
for i in range(1, 21, 1):
    if i % 2 == 0:
        print(i)

# Question 3:
print('\nQuestion 3:')
print('The sum of the numbers between 1 and 15 which are not divisible by 3 are: ')
sum1 = 0
for i in range(1, 16):
    if i % 3 != 0:
        sum1 = sum1 + i
print(sum1)

# Question 4:
print('\nQuestion 4:')
print('The product of all the even numbers between 2 and 30, which are divisible by 4 are: ')
product = 1
for i in range(2, 31):
    if i % 2 == 0 and i % 4 == 0:
        product = product * i
print(product)

# Question 1: - While Loop
number = int(input("Enter a number to be factorial-ed:   "))
i = 1
while number > 0:
    i = i * number
    number = number - 1
print('The factorial is:', i)
