# Nested FOR Loop.py
for i in range(0, 6):
    for j in range(0, i + 1):
        print('# ', end='')  # the end='' statement is used to override the default new line printed by default.
    print('')
print('\n')

number = 1
for i in range(0, 5):
    number = 1
    for j in range(0, i + 1):
        print(number, '', end='')
        number = number + 1
    print('')

print('\n')

number1 = 1
for i in range(0, 3):
    for j in range(0, i + 1):
        print(number1, '', end='')
        number1 = number1 + 1
    print('')
