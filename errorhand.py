__author__ = 'Avantha'
'''
myname = int(input('please enter the number:\n'))
print(myname) # retuns an exception error
'''
while True:
    try:
        myname = int(input('what is your number:\n'))
        print(18/myname)
        break
    except ValueError:
        print('you entered text')
    except ZeroDivisionError:
        print('you cant divide by 0')
    except: #This code will except any error not recomanded
        break
    finally:
        print('you did it')