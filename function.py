__author__ = 'Avantha'

def avantha():
    print('My first function - Multiply by 12')

def mcal(av):
    amnt=av*12
    return amnt # returns the answer to the equation when the function is called
    #print(amnt)

avantha()
a_av = int(input('please enter the number you want to multiply by 12: '))
av_ans = mcal(a_av)
print('you entered:', a_av)
print('when multiplied by 12 the answer is:', av_ans)


# this is to show how the default values can be stored in a function
def mynum(ads='Unknown'):
    if ads is 'Y':
        ads = 'correct'
    elif ads is 'N':
        ads = 'Incorrect'
    print(ads)

mynum('Y') # These lines will print the function with the defined value 'Y'
mynum('N') # These lines will print the function with the defined value 'Y'
mynum() # These lines will print the function when there is nothing defined in the function value

#--------------------------------
a = 20 # to access a variable by a function the variable has to be defined outside the function

def xl():
    #a = 20 defining the variable here wont work
    print(a)

# a = 20 defining the variable here will also work

def xy():
    print(a)
xl()
xy()
#---------------------------------------------
def myfn(a=0,b=0,c=0):
    out = a+b+c
    return out
    #print(out)

print('my functiona calculation is (a+b+c): ',myfn(2,3,5))
