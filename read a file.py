__author__ = 'Avantha'
# write
'''
fw = open('sample.txt','w')
fw.write('Itestt tetsts\n')
fw.write('THis is dam good\n')
fw.close()
'''
# read
fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()

# append
fa=open('sample.txt','a')
fa.write('\nthis is my second text')
fa.close()

# read a csv file and assign the valies to a lkist, then call them in to parameters to do a calculation
list=[]
fxl=open('Book1.csv','r')
text = fxl.read()
list=text.split(',')
#print(list)
print(list[1])
print(list[0])
c = int(list[1])+int(list[0])
print(c)

fxl.close()