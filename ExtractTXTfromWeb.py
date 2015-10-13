__author__ = 'Avantha'

import nltk
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime

def collect_data(url):
    html = urlopen(url).read()
    soup =BeautifulSoup(html,"html.parser")
    for script in soup(['script','style']):
        script.extract()
    text = soup.get_text()
    #text = str(soup.findAll('a',{'href'}))
    create_file(text)

# this will create a file and write rtext in to that
def create_file(my_text):
    full_date = datetime.datetime.now()
    dateStr = full_date.date()
    dest_url= 'Ads_'+str(dateStr)+'.txt'
    fx=open(dest_url,'w')
    fx.write(my_text)
    fx.close()


collect_data('http://edition.cnn.com/asia')
print('the file has been has been updated successfully!')

