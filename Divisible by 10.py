# Divisble by 10.py

list2 = []
for i in range(10):
    values = int(input('Enter the values to be used in the loop:  '))
    list2.append(values)

sum = 0
multiply = 1
for i in range(10):
    if list2[i] % 3 == 0:
       sum = sum + list2[i]
    else:
        multiply = multiply * list2[i]
print(f'The even values sum in the list are {sum}')
print(f'The odd values multiplied together are {multiply}')
