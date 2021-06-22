# CheckDigitChecker.py
multiplier = 1
total = 0

# Input a 13 digit ISBN number as a string
isbn = input('Input an ISBN-13 number with no spaces, the number has to be 13 digit:  ')

# Obtain the 13-digit (all characters in a string value are numbered from zero)
check_digit = int(isbn[12])
print('The check digit is:', check_digit)

# Iterate through the first 12 digits of the ISBN number
for i in range(12):
    total = total + (int(isbn[i]) * multiplier)
    print(total)
    if multiplier == 1:
        multiplier = 3

    else:
        multiplier = 1

remainder = total % 10
print('If 10 minus the remainder is equivalent to the check digit, the ISBN is valid.')
print('The remainder is', remainder)
if (10-remainder) == check_digit:
    print('The ISBN is valid')
else:
    print('The ISBN is not valid')
