__author__ = 'Avantha'

import random
import urllib.request

def download_immage(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

download_immage('http://www.supertechconsult.com/wp-content/uploads/2015/09/clive1.jpg')
