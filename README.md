# WebScaping Project
The main goal of this project is to provide a graphic interface to scrap CVE of products from the TOP50 vendor of CVEDetails, in order to produce output files in three formats to use them in an other context.
## DEPENDENCIES
- lxml
- Requests
- BeautifullSoup
### Install
```bash
pip install -r requirements.txt
```

## Functioning
This tool can be use with a graphic interface.
To use the graphic interface:
```
$ graph.py
```
You can click on the first menu to select the vendor from the top50 vendors that you want to get the products, then click on the second menu to select the product that you want to get the CVE. To launch webscraping, please select the "Start" button.
Once completed, the results can be consulted in produced files following the path VENDOR/PRODUCT/. The three formats supported are HTML, XML and JSON.

## commons.py
This file contains common ressources such as CVE class.
This class is used to provide a concrete object of a CVE containing the main informations.
The CVE_FIELDS class is an enumation containing a formating representation of CVE fields name.

## graph.py
This file contains the implementation of our graphic interface.

## parse_output.py
This file contains the implementation of the three output format.
- HTML
- XML
- JSON

## scraping.py
This file contains the implementation of our scraping engine. We use BeautifullSoup in order to parse the html reponse from the HTTP request. The main flaw of this file is that if the corresponding webpages change their structure, the script no longer works.

## TOP50 Vendor
Vendors are taken from the following URL: https://www.cvedetails.com/top-50-vendors.php

## Points for improvement
- Menus in this script are not user friendly, the solution is to use Combobox from the ttk lib instead of OptionMenu. We decided to keep that menu, due to lack of time. Some products can't be chosen because of that. 
- The script can't be used as commandline or API.
- We cannot choose between formats that are produced.