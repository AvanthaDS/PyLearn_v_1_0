__author__ = 'Avantha'

date,item,price = ['x','was bout on',2.21]
print(item)
print(date)
print(price)

def drop_f_last(grades):
    first,*middle,last=grades
    avg = sum(middle)/len(middle)
    print(avg)

drop_f_last([65,21,34,52,21,45])


