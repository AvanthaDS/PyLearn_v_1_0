__author__ = 'Avantha'

def calculate(a,b,c,x,y,z):
    ans_i = (b*z)-(y*c)
    ans_j = (a*z)-(x*c)
    ans_k = (a*y)-(x*b)
    print('--------------\nThe answer is:')
    print('A.B = '+ str(ans_i)+'i,'+str(ans_j)+'j,'+str(ans_k)+'k')

print('Simple Matrix calculator \nIf:')
print('A= [ai, bj, ck] \nB= [xi, yj, zk]\nTo calculate A.B:-')
print('Please enter the values below;')
count=0
m_list=[]
a_list=['a','b','c','x','y','z']
while count<6:
    m_list.append(int(input('Value for '+str(a_list[count])+':')))
    count+=1
calculate(*m_list)

#m_list=[int(input('a:')),int(input('b:')),int(input('c:')),int(input('x:')),int(input('y:')),int(input('z:'))]


