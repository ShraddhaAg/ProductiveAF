# coding: utf-8

import urllib2
from bs4 import BeautifulSoup
import re

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


array1 = []
array2 = []

p = ["https://medium.com/", "https://medium.com/search", "https://medium.com/membership?source=upgrade_membership---nav_full", "https://medium.com/m/signin?redirect=https%3A%2F%2Fmedium.com%2Ftag%2Fpython&source=--------------------------nav_reg&operation=login", "https://medium.com/m/signin?redirect=https%3A%2F%2Fmedium.com%2Ftag%2Fpython&source=--------------------------nav_reg&operation=register","https://medium.com/tag/programming", "https://medium.com/tag/python",'https://medium.com/tag/programming?source=related', u'https://medium.com/tag/data-science?source=related', u'https://medium.com/tag/machine-learning?source=related', u'https://medium.com/tag/django?source=related', "https://medium.com/tag/web-development?source=related", u'https://medium.com/tag/artificial-intelligence?source=related', u'https://medium.com/tag/deep-learning?source=related', u'https://medium.com/tag/software-development?source=related', u'https://medium.com/tag/coding?source=related','https://medium.com/tag/python/latest', u'https://medium.com/tag/python/archive' ,u'https://medium.com/tag/python-programming?source=related', u'https://medium.com/tag/python3?source=related', u'https://medium.com/@petrou.theodore', u'https://medium.com/@petrou.theodore?source=---------0---------------------', u'https://medium.com/dunder-data?source=---------0---------------------', u'https://medium.com/dunder-data/minimally-sufficient-pandas-a8e67f2a2428?source=---------0---------------------', u'https://medium.com/dunder-data/minimally-sufficient-pandas-a8e67f2a2428?source=---------0---------------------', u'https://medium.com/dunder-data/minimally-sufficient-pandas-a8e67f2a2428?source=---------0---------------------', u'https://medium.com/dunder-data/minimally-sufficient-pandas-a8e67f2a2428?source=---------0---------------------#--responses', u'https://medium.com/@petrou.theodore', u'https://medium.com/@petrou.theodore?source=---------3---------------------', u'https://medium.com/dunder-data?source=---------3---------------------', u'https://medium.com/dunder-data/minimally-sufficient-pandas-cheat-sheet-34f3a6888c36?source=---------3---------------------', u'https://medium.com/dunder-data/minimally-sufficient-pandas-cheat-sheet-34f3a6888c36?source=---------3---------------------', u'https://medium.com/dunder-data/minimally-sufficient-pandas-cheat-sheet-34f3a6888c36?source=---------3---------------------', u'https://medium.com/@aniruddha.choudhury94', u'https://medium.com/@aniruddha.choudhury94?source=---------8---------------------', u'https://medium.com/@aniruddha.choudhury94/stock-market-prediction-by-recurrent-neural-network-on-lstm-model-56de700bff68?source=---------8---------------------', u'https://medium.com/@aniruddha.choudhury94/stock-market-prediction-by-recurrent-neural-network-on-lstm-model-56de700bff68?source=---------8---------------------', u'https://medium.com/@aniruddha.choudhury94/stock-market-prediction-by-recurrent-neural-network-on-lstm-model-56de700bff68?source=---------8---------------------', u'https://medium.com/@aniruddha.choudhury94/stock-market-prediction-by-recurrent-neural-network-on-lstm-model-56de700bff68?source=---------8---------------------#--responses', u'https://medium.com/m/signin?redirect=https%3A%2F%2Fmedium.com%2Ftag%2Fdjango&source=--------------------------nav_reg&operation=login', u'https://medium.com/m/signin?redirect=https%3A%2F%2Fmedium.com%2Ftag%2Fdjango&source=--------------------------nav_reg&operation=register', 'https://medium.com/tag/django', 'https://medium.com/tag/api?source=related', 'https://medium.com/tag/python?source=related', 'https://medium.com/tag/javascript?source=related', u'https://medium.com/tag/docker?source=related', 'https://medium.com/tag/react?source=related', 'https://medium.com/m/signin?redirect=https%3A%2F%2Fmedium.com%2Ftag%2Freact&source=--------------------------nav_reg&operation=login', u'https://medium.com/m/signin?redirect=https%3A%2F%2Fmedium.com%2Ftag%2Freact&source=--------------------------nav_reg&operation=register']


djangoArray = []
reactArray = []

object = ["django","react"]

for tag in object:
    if tag == "django":
        url = "https://medium.com/tag/" + tag
        req = urllib2.Request(url, headers=hdr)
        html_page = urllib2.urlopen(req)
        soup = BeautifulSoup(html_page, 'html.parser')
        for link in soup.findAll('a', attrs={'href': re.compile("^https://medium.com/")}):
            array1.append(link.get('href'))
        for x in array1:
            if x not in p:
                djangoArray.append(x)

    if tag == "react":
        url = "https://medium.com/tag/" + tag
        req = urllib2.Request(url, headers=hdr)
        html_page = urllib2.urlopen(req)
        soup = BeautifulSoup(html_page, 'html.parser')
        for link in soup.findAll('a', attrs={'href': re.compile("^https://medium.com/")}):
            array2.append(link.get('href'))
        for y in array2:
            if y not in p:
                reactArray.append(y)


print djangoArray
print reactArray
