__author__ = 'Avantha'
import math

sqr = math.sqrt
print(sqr(4))

value = input('Please enter the Vale:')
diff = abs(17-int(value))
if int(value)>17:
    diff2 =diff*2
    print('Since the value >17 the new difference is : %i'%diff2)
else:
    print('The difference between the entered value and 17 is: %i'%diff)

def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))

a,b,c=input('PLease enter the three number')

if int(a)==int(b)==int(c):
    print(int(a)*3)
else:
    print(a)
    print(b)
    print(c)


