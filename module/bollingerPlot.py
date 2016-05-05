'''
Version: MRT v3.0
Type: module
Location: C:\MRT3.0\module
Author: Chintan Patel
Email: chintanlike@gmail.com

'''

# QSTK Imports
import module.qsdateutil as du
#import module.tsutil as tsu
import module.DataAccess as da

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np
#import basic
import modDatesReturn

def bollingerplotMain():
    '''Main Function'''
    # List of symbols
    #ls_symbols = ["AAPL", "GOOG", "IBM", "MSFT"]
    ls_symbols = list()

    symbol = str(raw_input('<<< Enter the list of symbol: '))
    symbols = symbol.upper()    
    ls_symbols.append(symbols)
            
    start_month,start_day,start_year,end_month,end_day,end_year = modDatesReturn.get_dates()    
    # We need closing prices so the timestamp should be hours=16.
    dt_timeofday = dt.timedelta(hours=16)

    # Get a list of trading days between the start and the end.
    
    dt_start = dt.datetime(start_year, start_month, start_day)
    dt_end = dt.datetime(end_year, end_month, end_day)
    # Creating an object of the dataaccess class with Yahoo as the source.
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
    c_dataobj = da.DataAccess('Yahoo')

    # Keys to be read from the data, it is good to read everything in one go.
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    # Reading the data, now d_data is a dictionary with the keys above.
    # Timestamps and symbols are the ones that were specified before.
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    # Copying close price into separate dataframe to find rets
    df_close = d_data['close']
    df_mean = pd.rolling_mean(d_data['close'], 20)
    df_std = pd.rolling_std(d_data['close'], 20)

    df_bollinger = (df_close - df_mean) / (df_std)
    print df_bollinger.tail()
    # Plotting the prices with x-axis=timestamps
    plt.clf()
    plt.subplot(211)
    plt.plot(ldt_timestamps, df_close[symbols], label=symbols)
    plt.legend()
    plt.ylabel('Price')
    plt.xlabel('Date')
    plt.xticks(size='xx-small')
    plt.xlim(ldt_timestamps[0], ldt_timestamps[-1])
    plt.grid(axis='both')
    plt.subplot(212)
    plt.plot(ldt_timestamps, df_bollinger[symbols], label='Bollinger')
    plt.axhline(1.0, color='r')
    plt.axhline(-1.0, color='r')
    plt.legend()
    plt.ylabel('Bollinger')
    plt.xlabel('Date')
    plt.xticks(size='xx-small')
    plt.xlim(ldt_timestamps[0], ldt_timestamps[-1])
    #plt.savefig('bollingerplot.pdf', format='pdf')

    plt.grid(axis='both')
    plt.show()

