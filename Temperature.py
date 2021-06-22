# Temperature.py
# Write a program to take in the temperature of 7 days, then find the maximum, minimum and average temperature.
temperature = []
for i in range(7):
     daily_temperature = int(input('Enter a temperature for the day:  '))
     temperature.append(daily_temperature)

max = temperature[0]
for i in range(7):
    if temperature[i] > max:
        max = temperature[i]
print(f'The maximum temperature in your list is {max}')

min = temperature[0]
for i in range(7):
    if temperature[i] < min:
        min = temperature[i]
print(f'The minimum temperature in your list is {min}')

total_temp = 0
for i in range(7):
    total_temp = total_temp + temperature[i]
average_temp = total_temp/7
print(f'The average temperature is {average_temp}')