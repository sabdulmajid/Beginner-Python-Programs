# Exam Style Questions.py
value = 0
nextValue = 0
value = int(input('Enter a value:  '))
nextValue = int(input('Enter the next value:  '))
while nextValue != 0:
    if nextValue > value:
        value = nextValue
print(value)
