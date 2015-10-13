__author__ = 'Avantha'

print('Simple Matrix calculator')
print('A= [ai, bj, ck] \nB= [xi, yj, zk]')

a = int(input('Please enter the value for a:'))
b = int(input('Please enter the value for b:'))
c = int(input('Please enter the value for c:'))
x = int(input('Please enter the value for x:'))
y = int(input('Please enter the value for y:'))
z = int(input('Please enter the value for z:'))

i = (b*z)-(c*y)
j = (a*z)-(c*x)
k = (a*y)-(b*x)

print('A ^ B = ['+ str(i)+'i, '+str(j)+'j, '+str(k)+'k]')

