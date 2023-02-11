#!/usr/bin/env python3
# -*- coding:Utf-8 -*-
import tkinter as tk
import tkinter.scrolledtext
import os
import main



BACKGROUND_COLOR = "#34495e"

DEFAULT_BUTTON_COLOR = "#bdc3c7"

ACTIV_BUTTON_COLOR = "#2ecc71"
ACTIV_FONT_COLOR = "#42e085"
ACTIV_BUTTON_COLOR_OVER = "#42e085"
ACTIV_FONT_COLOR_OVER = "#56f499"

DEACTIV_BUTTON_COLOR = "#c0392b"
DEACTIV_FONT_COLOR = "#fb6050"
DEACTIV_BUTTON_COLOR_OVER = "#d44d3f"
DEACTIV_FONT_COLOR_OVER = "#ff7464"

LABEL_COLOR = "#ecf0f1"

TEXT_BACKGROUND_COLOR = "#2c3e50"

SCAN_PATH = ""

# app frame
app = tk.Tk()
app.geometry("600x400")
app.title("WEBSCRAPING tool")
app.configure(bg=BACKGROUND_COLOR)

def selected_option1(value):
    print("Option 1:", value)

def selected_option2(value):
    print("Option 2:", value)


label = tk.Label(app, text="Choissisez un vendeur, puis un produit")
label.config(width=90, height=2)
label.pack()

var1 = tk.StringVar()
var2 = tk.StringVar()

options1 = ["Option 1A", "Option 1B", "Option 1C"]
options2 = ["Option 2A", "Option 2B", "Option 2C"]

menu1 = tk.OptionMenu(app, var1, *options1, command=lambda value: selected_option1(value),)
menu1.config(width=60, height=1,)
menu1.pack(pady=40)

menu2 = tk.OptionMenu(app, var2, *options2, command=lambda value: selected_option2(value))
menu2.config(width=60, height=1,)
menu2.pack(pady=40)


button = tk.Button(app, text="Start", command=lambda value: startButtonFunction(app))
button.config(width=10, height=1)
button.pack(pady=10)


app.mainloop()
