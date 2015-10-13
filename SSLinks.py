__author__ = 'Avantha'

import requests
from bs4 import BeautifulSoup

def my_spider():
    #page = 1
    #while page<= max_page:
    url ='http://www.getagility.com.au'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for link in soup.findAll('a'):
        linktit = link.string
        href = link.get('href')
        print(linktit)
        print(href)
my_spider()