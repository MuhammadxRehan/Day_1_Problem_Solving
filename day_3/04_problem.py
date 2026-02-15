# Write a Python program to check whether a given year is a leap year.


def leat_year(year):
    if year % 4 == 0:
        print('It is a leap year')
    else:
        print('It is not a leap year') 


year = int(input('Enter a year: '))

leat_year(year)