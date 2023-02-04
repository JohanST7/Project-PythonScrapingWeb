#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.cvedetails.com/top-50-vendors.php'

response = requests.get(url)

items = ''

if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all("table", class_="listtable").find_all("td", class_=None)
    print(items)



items.find_all("td", class_=None)

news_items = []

for i in items :
    news_i={}
    news_i ['title'] = items.title.text
    news_i ['description'] = items.description.text
    news_i ['pubdate'] = items.pubdate.text
    news_items.append(news_i)

df=pd.DataFrame(news_items,columns=['vendor Name','Number of Products','Number of Vulnerabilities'])