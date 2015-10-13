__author__ = 'Avantha'
import math

n = input('please enter value for n:')

nn= int(str(n)+str(n))
nnn=int(str(n)+str(n)+str(n))

print(int(n)+nn+nnn)

Val = int(n) % 2

if Val>0:
    print('THis is an Odd number')
else:
    print('This is an even Number')

#------------------------------------
def new_string(str):
  if len(str) >= 2 and str[:2] == "Is":
    return str
  return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))

#------------------------------------
def stri(st,n):
    text = ""
    for i in range(n):
        text = text+st
    return text

print(stri('Apple\n',5))

#--------------------------------------
def counter(num):
    count = 0
    for i in num:
        if i == 4:
            count = count+1
        i=i+1
    return count

list = [2,3,4,5,4,3,4,12,4,5,5,6,7,8,9,3,2,4,2,4,2,3,4,2,1,1,7,6,6,2]

print('the number of time "4" appears is',counter(list))

#---------------------------------------
def string(sa,a):
    if len(sa) >= 2:
        while a > 0:
            print(str(sa[:2]))
            a=a-1
    else:
        while a > 0:
            print(sa)
            a=a-1

string('My Name is Avantha',5)

#-----------------------------------------
lst = ['a','e','i','o','u','A','E','I','O','U']

def chk(let):
    if let in lst:
        print('This is a Vowel')
    else:
        print('Not a Vowel')

let =input('Please enter the letter here:')
chk(let)
