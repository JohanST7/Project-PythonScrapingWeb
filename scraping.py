#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from commons import CVE

def getVendors():
    vendors = []
    url = 'https://www.cvedetails.com/top-50-vendors.php'
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find("table", class_="listtable")
        for i in items.find_all("tr"):
            if len(i.find_all("th")) == 0:
                #Name
                name = i.find_all("td")[1].find("a").text
                #Link
                link = i.find_all("td")[2].find("a")["href"]
                vendors.append((name,link))
    return vendors

def getProducts(vendor):
    products = []
    baseURL = "https://www.cvedetails.com"
    url = baseURL + vendor[1]
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find("table", class_="listtable")
        for i in items.find_all("tr"):
            if len(i.find_all("th")) == 0:
                #Name
                name = i.find_all("td")[0].find("a").text
                #Link
                link = i.find_all("td")[2].find("a")["href"]
                products.append((name,link))
    return products

def getCVE(product):
    cves = []
    baseURL = "https://www.cvedetails.com"
    url = baseURL + product[1]
    response = requests.get(url)
    table = ""
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find("table",class_="searchresults sortable")
        items = soup.find_all("tr", class_="srrowns")
        for cve in items:
            cve_info = cve.find_all("td")

            CVE_ID = cve_info[1].find("a").text
            vType = cve_info[4].text
            pDate = cve_info[5].text
            uDate = cve_info[6].text
            score = cve_info[7].find("div").text
            gainedAccessLevel = cve_info[8].text
            access = cve_info[9].text
            complexity = cve_info[10].text
            authentication = cve_info[11].text
            confidentiality = cve_info[12].text
            integrity = cve_info[13].text
            availability = cve_info[14].text
            #Link
            link = cve_info[1].find("a")["href"]
            # append tuple (CVE, link_to_cve)
            cves.append((CVE(CVE_ID,vType,pDate,uDate,score,gainedAccessLevel,access,complexity,authentication,confidentiality,integrity,availability),
                        baseURL+link))
    return (cves, table.prettify())