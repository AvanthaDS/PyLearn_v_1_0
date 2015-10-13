__author__ = 'Avantha'


import datetime

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        full_date = datetime.datetime.now()
        dateStr = full_date.date()
        filename= 'av_'+str(dateStr)+'.txt'

        plain_text1 = 'My Text1'
        plain_text2 = 'My Text2'

        print(plain_text1)
        print(plain_text2)
        fx=open(filename,'a') # write -'w', append-'a', read-'r'
        fx.write(plain_text1+'\n')
        fx.write(plain_text2+'\n')


        page += 1

trade_spider(1)
print('the file has been created successfully')
input('please enter any key to exit')