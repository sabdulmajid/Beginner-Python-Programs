# volume_calculator_of_aquarium.py

#User inputs the dimensions of the tank
height_h = int(input('Enter the height of the aquarium, in cm '))
width_w = int(input('Enter the width of the aquarium, in cm '))
length_l = int(input('Enter the length of the aquarium, in cm '))

volume_aquarium = length_l * width_w * height_h

# Conversion of cm^3 to litres
volume_aquarium_litres = volume_aquarium/1000

# Final result i.e the volume
print('The volume is:')
print(volume_aquarium_litres, 'litres')

# Allow user to finish
input('Press ENTER to finish the program')