# ImportingFromDateTime.py
from datetime import datetime


def validate_date(d):
    while True:
        try:
            return datetime.strptime(d, '%d/%m/%Y')
        except:
            d = input('Date must be in the dd/mm/yyyy format, please enter the correct data:  ')


date = input('Please enter  date: ')
date = validate_date(date)
