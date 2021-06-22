# Exam Style Questions - 2.py
total = 1
count = 0
while count < 3:
    number = float(input('Enter a number:  '))
    total = total * number
    count = count + 1

average = total/count
print('Average = ', average)
