#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.cvedetails.com/top-50-vendors.php'

response = requests.get(url)

items = ''

urls = []

if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find("table", class_="listtable")
    for i in items.find_all("tr"):
        if len(i.find_all("th")) == 0:
            #Name
            print(i.find_all("td")[1].find("a").text)
            #link
            print(i.find_all("td")[2].find("a")["href"])
        

print('------------')

url = 'https://www.cvedetails.com/top-50-products.php'

response = requests.get(url)

items = ''
'''
if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find("table", class_="listtable")
    for i in items.find_all("td", class_=None):
        print(i.text)'''