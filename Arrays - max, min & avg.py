# Arrays - max, min & avg.py
number_elements = int(input('Enter the number of elements to be inputted into the array:  '))
array = []
for i in range(number_elements):
    user_input = int(input('Enter an element to add to the array:  '))
    array.append(user_input)

max = array[0]
for i in range(number_elements):
    if array[i] > max:
        max = array[i]
print(f'The maximum value in your array is {max}')

min = array[0]
for i in range(number_elements):
    if array[i] < min:
        min = array[i]
print(f'The minimum value in your array is {min}')

average = sum(array)/len(array)
print(f'Your average value for this list is {round(average, 2)}, to two decimal places.')
