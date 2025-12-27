'''
Version: MRT v3.0
Type: module
Location: C:\MRT3.0\module
Author: Chintan Patel
Email: chintanlike@gmail.com

Pulling Yahoo CSV Data
'''

try:
    import urllib.request as urllib2
    import urllib.parse as urllib
except Exception:
    import urllib2
    import urllib
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

        symbol_data=list()
        # print("Getting {0}".format(symbol)
        
        try:
            params= urllib.urlencode ({'a':0, 'b':1, 'c':2010, 'd':_now.month, 'e':_now.day, 'f':_now.year, 's': symbol})
            url = "http://ichart.finance.yahoo.com/table.csv?%s" % params
            url_get= urllib2.urlopen(url)
            
            header= url_get.readline()
            symbol_data.append (url_get.readline())
            while (len(symbol_data[-1]) > 0):
                symbol_data.append(url_get.readline())
            
            symbol_data.pop(-1) #The last element is going to be the string of length zero. We don't want to write that to file.
            #now writing data to file
            os.chdir(data_path)
            f = open (symbol_name + ".csv", 'w')
            
            #Writing the header
            f.write (header)
            
            while (len(symbol_data) > 0):
                f.write (symbol_data.pop(0))
             
            f.close();    

        
        except urllib2.HTTPError:
            miss_ctr += 1
            print("<<<(w) Unable to fetch data for stock: {0}".format(symbol_name))
        except urllib2.URLError:
            miss_ctr += 1
            print("<<<(w) URL Error for stock: {0}".format(symbol_name))
            
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
   
