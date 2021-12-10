#Stock Data Api GUI

import tkinter as tk
from tkinter.constants import BOTTOM, CENTER
import yahoo_fin as si 
import yahoo_fin.stock_info as si 

root=tk.Tk()

root.title('Stock Tracker')

root.configure(bg='#045D5D')

root.geometry('600x525')

Stocklabel =tk.Label(root, bg='white', font='courier', justify='left')
Stocklabel.pack()

ticker_entry=tk.Entry(root, bg='#045D5D')
ticker_entry.place(y=445, x=240)

def getstock():
    quote_table = si.get_quote_table((ticker_entry.get()), dict_result=False)
    quote_table
    
    Stocklabel['text'] = quote_table

def getaapl():
    quote_table = si.get_quote_table('AAPL', dict_result=False)
    quote_table
    
    Stocklabel['text'] = quote_table

def getmsft():
    quote_table = si.get_quote_table('MSFT', dict_result=False)
    quote_table
    
    Stocklabel['text'] = quote_table

def getgoog():
    quote_table = si.get_quote_table('GOOG', dict_result=False)
    quote_table
    
    Stocklabel['text'] = quote_table

def getamzn():
    quote_table = si.get_quote_table('AMZN', dict_result=False)
    quote_table
    
    Stocklabel['text'] = quote_table

def getnvda():
    quote_table = si.get_quote_table('NVDA', dict_result=False)
    quote_table
    
    Stocklabel['text'] = quote_table

def gettsla():
    quote_table = si.get_quote_table('TSLA', dict_result=False)
    quote_table
    
    Stocklabel['text'] = quote_table

stock = tk.Button(root, text ='Get Data', command=getstock, width=10)
stock.pack(side=BOTTOM)

getaaplbtn = tk.Button(root, text ='APPLE', command=getaapl, width=10)
getaaplbtn.place(y=340, x=220)

getmsftbtn = tk.Button(root, text ='MSFT', command=getmsft, width=10)
getmsftbtn.place(y=365, x=220)

getgoogbtn = tk.Button(root, text ='GOOGLE', command=getgoog, width=10)
getgoogbtn.place(y=390, x=220)

getamznbtn = tk.Button(root, text ='AMAZON', command=getamzn, width=10)
getamznbtn.place(y=340, x=300)

getnvdabtn = tk.Button(root, text ='NVIDIA', command=getnvda, width=10)
getnvdabtn.place(y=365, x=300)

gettslabtn = tk.Button(root, text ='TESLA', command=gettsla, width=10)
gettslabtn.place(y=390, x=300)

root.mainloop()