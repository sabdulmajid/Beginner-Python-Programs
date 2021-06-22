# Importing-Time.py
# Import the time module into the program:
from time import *


prime = True

number = int(input('Enter number to test:   '))

# Grab start time
start_time = time()

counter = 2
while counter < number-1 and prime is True:
    modulus = number % counter
    if modulus == 0:
        prime = False
    counter = counter + 1
    # The next line is to see whether processing is going on
    print(counter)


if prime is True:
    print('Your number is PRIME')
else:
    print('Your number is NOT PRIME')

# Print out the current time minus the start_time
print('This took', (time()-start_time), 'seconds')
