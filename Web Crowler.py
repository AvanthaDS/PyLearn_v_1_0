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
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser") # Chec the error you get when the html parser is not added
        for link in soup.findAll('a',{'class':'yt-uix-sessionlink yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2       spf-link '}):
            title = link.string
            href = 'https://www.youtube.com/'+link.get('href')
            print(title)
            print(href)

            get_single_item_data(href)
        page += 1

def get_single_item_data(item_url): # this is a nother funtion that goes in to the page and find the contentr
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for item_name in soup.findAll('strong',{'class':'watch-time-text'}):
          print(item_name.string)


trade_spider(1)
time.sleep(10)

