__author__ = 'Avantha'

import requests
from bs4 import BeautifulSoup

def my_spider(max_page):
    page = 1
    while page<= max_page:
        url ='https://m.hays.com.au/search/?q=hays&specialismId=IT&p='+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        for link in soup.findAll('a',{'class':'label'}):
            linktit = link.string
            href = 'https://m.hays.com.au/'+link.get('href')
            if linktit in 'WA, Perth':
                print(linktit)
                print(href)
            #wapage_sp(href)
        page +=1
'''
def wapage_sp(wapage):
    source_code = requests.get(wapage)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for walink in soup.findAll('a',{'class':'label'}):
        m_wa_linkstr = walink.string
        m_wa_link = 'https://m.hays.com.au/'+ walink.get('href')
        print(m_wa_link)
        print(m_wa_linkstr)
'''
my_spider(1)








