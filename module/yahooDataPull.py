'''
Version: MRT v3.0
Type: module
Author: Chintan Patel
Email: chintanlike@gmail.com

Pulling Yahoo CSV Data
'''

import yfinance as yf
import datetime
import os
from module import basic
import time

def get_data(data_path,ls_symbols):

    # Create path if it doesn't exist
    if not (os.access(data_path, os.F_OK)):
        os.makedirs(data_path)

    # utils.clean_paths(data_path)   

    _now =datetime.datetime.now();
    miss_ctr=0; #Counts how many symbols we could not get
    for symbol in ls_symbols:
        # Preserve original symbol since it might
        # get manipulated if it starts with a "$"
        symbol_name = symbol
        if symbol[0] == '$':
            symbol = '^' + symbol[1:]

        # print("Getting {0}".format(symbol))
        
        try:
            start_date = '2010-01-01'
            end_date = _now.strftime('%Y-%m-%d')
            df = yf.download(symbol, start=start_date, end=end_date)
            if df.empty:
                miss_ctr += 1
                print("<<<(w) Unable to fetch data for stock: {0}".format(symbol_name))
            else:
                df.to_csv(os.path.join(data_path, symbol_name + '.csv'))
        
        except Exception as e:
            miss_ctr += 1
            print("<<<(w) Error fetching data for stock: {0} - {1}".format(symbol_name, str(e)))
            
    print("All done. Got {0} stocks. Could not get {1}".format(len(ls_symbols) - miss_ctr, miss_ctr))

def read_symbols(s_symbols_file):

    ls_symbols=[]
    file_symbol = open(s_symbols_file, 'r')
    for line in file_symbol.readlines():
        str_line = str(line)
        if str_line.strip(): 
            ls_symbols.append(str_line.strip())
    file_symbol.close()
    
    return ls_symbols  

def yahooDatamain():
    path = os.getcwd()
    print(path)
    symbol_file = os.path.join(path,"MRT_SYMBOLS.txt")
    if os.path.isfile(symbol_file):
        ls_symbols = read_symbols(symbol_file)
        download_path = os.path.join(path,'Data','Yahoo')
        get_data(download_path, ls_symbols)
    else:
        print('<<<(w) File Not Found: MRT_SYMBOLS.txt ')
        time.sleep(2)
        basic.go_back()
   
