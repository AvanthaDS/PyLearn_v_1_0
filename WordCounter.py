__author__ = 'Avantha'
import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for post_text in soup.findAll('a',{'class':'label'}):
        content = post_text.string
        words = content.lower().split() # if the retun data has blanks this wont work
        for each_word in words:
            #print(each_word)
            word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = '!@#$%~^&*()_+>":-=,./][\"""'
        for i in range(0,len(symbols)):
            word = word.replace(symbols[i],"")
        if len(word)>0:
            #print(word)
            clean_word_list.append(word)

    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word]= 1
    for key,value in sorted(word_count.items(), key=operator.itemgetter(0)):
        # on the above line whe 0 is entered the list will be orderd by the key and when used '1' it will be ordered by the value
        print(key,value)

start('https://m.hays.com.au/search/?q=hays&specialismId=Engine')