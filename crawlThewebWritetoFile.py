__author__ = 'Avantha'

import requests
from bs4 import BeautifulSoup
import datetime
import time

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url ='https://www.youtube.com/results?search_query=VW+Scandal&page='+str(page)
        source_code = requests.get(url)
        full_date = datetime.datetime.now()
        dateStr = full_date.date()
        filename= 'fl_'+str(dateStr)+'.txt'

        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser") # Chec the error you get when the html parser is not added
        for link in soup.findAll('a',{'class':'yt-uix-sessionlink yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2       spf-link '}):
            title = link.string
            href = 'https://www.youtube.com/'+link.get('href')
            print(title)
            print(href)
            fx=open(filename,'a') # write -'w', append-'a', read-'r'
            fx.write(title+'\n')
            fx.write(href+'\n')


            source_code2= requests.get(href)
            plain_text2=source_code2.text
            soup2=BeautifulSoup(plain_text2,"html.parser")
            for item_name in soup2.findAll('strong',{'class':'watch-time-text'}):
                print(item_name.string)
                fx.write(item_name.string+'\n\n')
                fx.close()

        page += 1

trade_spider(2)
time.sleep(5)