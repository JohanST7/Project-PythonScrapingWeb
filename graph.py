#!/usr/bin/env python3
# -*- coding:Utf-8 -*-
import tkinter as tk
import tkinter.scrolledtext
import os
import scraping
from parse_output import parse

# Static variables
VENDORS = [""]
PRODUCTS = [""]
CVES = [""]

# Static colors
BACKGROUND_COLOR = "#34495e"
DEFAULT_BUTTON_COLOR = "#bdc3c7"

# Element functions
def selected_vendor(value):
    global PRODUCTS
    PRODUCTS.clear()
    global product_list
    product_list.clear()
    global menu2
    menu2.children["menu"].delete(0,"end")
    for i in VENDORS:
        vendor_name = i[0]
        if vendor_name == value:
            PRODUCTS = scraping.getProducts(i)
    for i in PRODUCTS:
        product_name = i[0]
        product_list.append(product_name)
        menu2.children["menu"].add_command(label=product_name,command=lambda value=product_name: selected_product(value))

def selected_product(value):
    stringVar_product.set(value)

def startButtonFunction(value):
    prod = value.get()
    CVES = []
    for i in PRODUCTS:
        if i[0] == prod:
            #CVES = (CVES, html_table)
            CVES = scraping.getCVE(i)
    parse(stringVar_vendor.get(), stringVar_product.get(), CVES)

# Other funtions
def init():
    # Init list of tuple (vendor_name,link_to_products)
    global VENDORS
    VENDORS = scraping.getVendors()
    # Init list of vendors
    for i in VENDORS:
        vendor_list.append(i[0])

# app frame
app = tk.Tk()
app.geometry("600x400")
app.title("WEBSCRAPING tool")
app.configure(bg=BACKGROUND_COLOR)
# Banner label
label = tk.Label(app, text="Choissisez un vendeur, puis un produit")
label.config(width=90, height=2)
label.pack()

# String variables 
stringVar_vendor = tk.StringVar()
stringVar_product = tk.StringVar()

vendor_list = [""]
product_list = [""]

init()

menu1 = tk.OptionMenu(app, stringVar_vendor, *vendor_list, command=lambda value: selected_vendor(value))
menu1.config(width=60, height=1)
menu1.pack(pady=40)

menu2 = tk.OptionMenu(app, stringVar_product, *product_list)
menu2.config(width=60, height=1)
menu2.pack(pady=40)

button = tk.Button(app,relief="flat", text="Start",bg=DEFAULT_BUTTON_COLOR,font=("Arial Black",20), command=lambda value=stringVar_product: startButtonFunction(value))
button.config(width=10, height=1)
button.pack(pady=10)

app.mainloop()
