import calendar                             #This module contains functions for calender
year = int(input('Enter the year'))         #Input values
month = int(input('Enter the month'))
print(calendar.month(year,month))
print(calendar.__doc__)                     #Print 