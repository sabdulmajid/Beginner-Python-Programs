# User_Journey.py

kilometers = int(input('Please enter the distance of your journey: '))

while kilometers < 15:
    kilometers = int(input('Please input a valid value over 15 kilometers: '))

fuel = kilometers * 100

print(f'Your total fuel required: {fuel}')
