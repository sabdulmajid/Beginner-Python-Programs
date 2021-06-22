# Question_7.py

# User inputs data.
gender = bool(input('Enter your gender. If you are male, enter True. If not, enter False.  '))
age = int(input('Enter your age  '))
marital_status = str(input('Are you married or not? If you are, type yes. If not, type no.  '))

if gender is True and 20 <= age <= 40:
    print('You are allowed to work anywhere you like!')
elif gender is False:
    print('You can only work in urban areas.')
elif gender is True and 40 < gender <= 60:
    print('You can only work in urban areas.')
else:
    print('ERROR 404! You are either too young to work or too old to work.')
    


    