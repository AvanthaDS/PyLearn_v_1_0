import requests
from bs4 import BeautifulSoup
import operator

a_list=[]
clean_list=[]

def start(url):
    code = requests.get(url)
    plain_text = code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for all_text in soup.findAll('a',{'class':'yt-uix-sessionlink yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2       spf-link '}):
    #for all_text in soup.findAll(attrs={'class'}):
        content = all_text.string
        a_list.append(content.split())
    print(content)
    print(*a_list)


start('https://www.youtube.com/results?search_query=VW+Scandal&page=1')

while True:
    srch = str(input('Please enter the word you want to search:'))
    print(srch)
    try:
        if str(srch) in str(a_list):
            print('You found a match')
            break
        else:
            print('Sorry, No match found!\n')

    finally:
        print('')