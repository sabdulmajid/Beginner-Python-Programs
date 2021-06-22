# ConversionofDHSintoS.py

SECONDSINMINUTE = 60
SECONDSINHOUR = 60*60
SECONDSINDAY = 60*60*24

numberofdays = int(input('Enter the number of days:  '))
numberofhours = int(input('Enter the number of hours:  '))
numberofminutes = int(input('Enter the number of minutes:  '))
numberofseconds = int(input('Enter the number of seconds:  '))

total_number_of_seconds = numberofdays * SECONDSINDAY
total_number_of_seconds = total_number_of_seconds + (numberofhours * SECONDSINHOUR)
total_number_of_seconds = total_number_of_seconds + (numberofminutes * SECONDSINMINUTE)
total_number_of_seconds = total_number_of_seconds + numberofseconds

print('Total number of seconds: ', '%d' % total_number_of_seconds)


# Python Program to Convert seconds
# into hours, minutes and seconds

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)


# Driver program
n = int(input('Enter a the number of seconds to be converted into hours, minutes and secs:  '))
print(convert(n))
