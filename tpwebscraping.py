#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.cvedetails.com/top-50-vendors.php'

response = requests.get(url)

items = ''

if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find("table", class_="listtable")
    for i in items.find_all("td", class_=None):
        print(i.text)

#Scrap la page du vendor Microsoft pour récupérer ses products

url = 'https://www.cvedetails.com/product-list/vendor_id-26/Microsoft.html'

responsep = requests.get(url)

if responsep.ok:
    soup = BeautifulSoup(responsep.text, 'lxml')
    product = soup.find("table", class_="listtablecontainer")
    productb = soup.a(<a class="listtablecontainer" href="/product-list/product_type-/firstchar-/vendor_id-26/page-1/products-by-name.html?sha=5490ab64aaaeac45d7701eff5f1fd2da7c24e1a5&amp;order=1&amp;trc=722" id="link1"> Product Name </a>)
    
    for p in product.find_all("td", class_=None):
        print(p.text)
    for p in productb.find_all("td", class_=None):
        print(p.text)



print('------------')

url = 'https://www.cvedetails.com/top-50-products.php'

response = requests.get(url)

items = ''

if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find("table", class_="listtable")
    for i in items.find_all("td", class_=None):
        print(i.text)
