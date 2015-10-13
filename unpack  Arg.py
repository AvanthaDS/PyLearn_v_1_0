__author__ = 'Avantha'

def caculate(a,b,c,d):
    answer = 100-a+b+(c*d)
    print(answer)

av_list =[12,10,3,4]

#caculate(av_list[0],av_list[1],av_list[2],av_list[3])
caculate(*av_list) # this unpacks the numbers in to the function variables

def lista(*args):
    sim = 0
    for a in args:
        sim += a
    print(sim)

lista(12,32,6)

