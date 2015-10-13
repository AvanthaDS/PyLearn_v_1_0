__author__ = 'Avantha'

answer = lambda x:x*7
print(answer(7))

ads = lambda x,y,z:x+y+z

print(ads(int(input('please enter x: ')),int(input('please enter y: ')),int(input('please enter z: '))))


#----------- the following is a useless function but the above can be handy Still it works like the following
xyz = lambda a,b:(a+b)/b

a= int(input('please enter a:'))
b= int(input('please enter b:'))

print(xyz(a,b))

