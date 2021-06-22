# Pyramid Program.py
def func():
    symbol = input('Enter a symbol to make a pyramid out of: ')
    maxSymbols = int(input('Enter the maximum number of symbols you want: '))
    while maxSymbols % 2 == 0:
        maxSymbols = input('Invalid. Please enter an odd number: ')
    spaces = (maxSymbols - 1)/2
    numberSymbols = 1

    while numberSymbols <= maxSymbols:
        for i in range(int(spaces)):
            print('')
            
            for j in range(maxSymbols):
                print(symbol)
                
        spaces -= 1
        numberSymbols += 2
        print('')


symbol = input('The symbol you want: ')
number_of_rows = int(input('Number of rows: '))
number_of_spaces = number_of_rows - 1

for i in range(0, number_of_rows):
    for j in range(0, number_of_spaces):
        print(end=' ')
    number_of_spaces = number_of_spaces - 1
    for j in range(0, i+1):
        print(f"{symbol}", end=' ')
    print('\r')


