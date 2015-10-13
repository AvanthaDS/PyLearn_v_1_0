__author__ = 'Avantha'
'''
av = 5
while av<10:
    print('avantha')
    av +=1
'''
'''ads = int(input('Please enter a number here:'))
for n in range(50):
    if n is ads:
        print(n,'is the number you entered')
        break
    else:
        print(n)
'''

'''
# this was the homework given by Bukky
for n in range(101):
    if n%4 is 0:
        print(n)
'''

av = [12,11,17,8,5]
print('These are teh numbers available:')
for n in range(1,20):
    if n in av:
        continue
    print(n)