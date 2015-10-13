__author__ = 'Avantha'

import calendar
import datetime

from datetime import date


today = datetime.date.today()
print(today)
datelst = str(today)
lst = datelst.split('-')
y = int(lst[0])
m = int(lst[1])
'''
y = int(input('Please enter trhe year:'))
m = int(input('Please enter the month:'))
'''
print('The calendar of this month')
cal = calendar.month(y,m)
print(cal)
print('''This is a string that
can be written in
mutple lines... how cool is that''')

ab = input('Please enter the first date YYYY,MM,DD: ')
bb = input('Please enter the second date YYYY,MM,DD: ')
ablist =ab.split(',')
bblist =bb.split(',')

a = date(int(ablist[0]),int(ablist[1]),int(ablist[2]))
b = date(int(bblist[0]),int(bblist[1]),int(bblist[2]))

print(a,b)
print((a-b).days)

