__author__ = 'Avantha'
mylist = {'bun','marmite','shampoo','banana','bun'}
print(mylist)

newitem = input('Please enter your item:')


if newitem in mylist:
    print('this is already there in the list')
else:
    print('yes you need ',newitem)

# dictionaries-----------------------

people = {'Tony':'-is not my friend','Tharanga':'-she is my lovely wife','Lal':'-He is my father'}

#print(people)

print(people['Tharanga'])

for k,v in people.items():
    print(k+v)