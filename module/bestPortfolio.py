'''
Version: MRT v3.0
Type: module
Location: C:\MRT3.0\module
Author: Chintan Patel
Email: chintanlike@gmail.com

Get Best Portfolio from 4 Symbols

'''

# QSTK Imports
import module.qsdateutil as du
import module.tsutil as tsu
import module.DataAccess as da

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
#import pandas as pd
import numpy as np
import basic
import modDatesReturn


def simulate(na_rets, lf_alloc):
    ''' Simulate Function'''
    # Estimate portfolio returns
    na_portrets = np.sum(na_rets * lf_alloc, axis=1)
    cum_ret = na_portrets[-1]
    tsu.returnize0(na_portrets)

    # Statistics to calculate
    stddev = np.std(na_portrets)
    daily_ret = np.mean(na_portrets)
    sharpe = (np.sqrt(252) * daily_ret) / stddev

    # Return all the variables
    return stddev, daily_ret, sharpe, cum_ret


def bestPort():
    '''Main Function'''
    # List of symbols
    #ls_symbols = ["AXP", "HPQ", "IBM", "HNZ"]
    ls_symbols = list()
    
    try:
        len_sym = input('<<< How many symbol(Works only for 4 symbols):  ')
        if len_sym > 4 or len_sym <= 0 or len_sym < 4:
            print '<<<(w) Works only for 4 symbols..\n'
            basic.print_logo()
            basic.print_clrscr()
            basic.go_back()        

    except ValueError:
        basic.print_logo()
        basic.print_clrscr()
        basic.go_back()
    except SyntaxError:
        basic.print_logo()
        basic.print_clrscr()
        basic.go_back()
    except NameError:
        basic.print_logo()
        basic.print_clrscr()
        basic.go_back()
    

    
    for i in range(len_sym):
        symbols = str(raw_input('<<< Enter the list of symbols: '))
        ls_symbols.append(symbols)

    ## Start and End date of the charts
 
    start_month,start_day,start_year,end_month,end_day,end_year = modDatesReturn.get_dates()
    dt_start = dt.datetime(start_year, start_month, start_day)
    dt_end = dt.datetime(end_year, end_month, end_day)
    # Start and End date of the charts
    #dt_start = dt.datetime(2010, 1, 1)
    #dt_end = dt.datetime(2010, 12, 31)

    # We need closing prices so the timestamp should be hours=16.
    dt_timeofday = dt.timedelta(hours=16)

    # Get a list of trading days between the start and the end.
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

    # Creating an object of the dataaccess class with Yahoo as the source.
    c_dataobj = da.DataAccess('Yahoo')

    # Keys to be read from the data, it is good to read everything in one go.
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

    # Reading the data, now d_data is a dictionary with the keys above.
    # Timestamps and symbols are the ones that were specified before.
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    # Copying close price into separate dataframe to find rets
    df_rets = d_data['close'].copy()
    # Filling the data.
    df_rets = df_rets.fillna(method='ffill')
    df_rets = df_rets.fillna(method='bfill')

    # Numpy matrix of filled data values
    na_rets = df_rets.values
    na_rets = na_rets / na_rets[0, :]
    
    lf_alloc = [0.0, 0.0, 0.0, 0.0]

    max_sharpe = -1000
    final_stddev = -1000
    final_daily_ret = -1000
    final_cum_ret = -1000
    best_portfolio = lf_alloc

    for i in range(0, 101, 10):
        left_after_i = 101 - i
        for j in range(0, left_after_i, 10):
            left_after_j = 101 - i - j
            for k in range(0, left_after_j, 10):
                left_after_k = 100 - i - j - k
                lf_alloc = [i, j, k, left_after_k]
                lf_alloc = [x * 0.01 for x in lf_alloc]
                stddev, daily_ret, sharpe, cum_ret = simulate(na_rets, lf_alloc)
                if sharpe > max_sharpe:
                    max_sharpe = sharpe
                    final_stddev = stddev
                    final_cum_ret = cum_ret
                    final_daily_ret = daily_ret
                    best_portfolio = lf_alloc

    print "<<< Symbols : ", ls_symbols
    print "<<< Best Portfolio : ", best_portfolio
    print "<<< Statistics : Std. Deviation : ", final_stddev
    print "<<< Statistics : Daily Returns  : ", final_daily_ret
    print "<<< Statistics : Cum. Returns   : ", final_cum_ret
    print "<<< Statistics : Sharpe Ratio   : ", max_sharpe
##
##    ls_symbols_toread = list(set(ls_symbols) | set(['SPY']))
##
##    # Reading the data, now d_data is a dictionary with the keys above.
##    # Timestamps and symbols are the ones that were specified before.
##    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols_toread, ls_keys)
##    d_data = dict(zip(ls_keys, ldf_data))
##
##    # Copying close price into separate dataframe to find rets
##    df_rets = d_data['close'].copy()
##    # Filling the data.
##    df_rets = df_rets.fillna(method='ffill')
##    df_rets = df_rets.fillna(method='bfill')
##
##    df_rets = df_rets.reindex(columns=ls_symbols)
##
##    # Numpy matrix of filled data values
##    na_rets = df_rets.values
##    # returnize0 works on ndarray and not dataframes.
##    tsu.returnize0(na_rets)
##
##    # Estimate portfolio returns
##    na_portrets = np.sum(na_rets * best_portfolio, axis=1)
##    na_port_total = np.cumprod(na_portrets + 1)
##
##    na_market = d_data['close']['SPY'].values
##    na_market = na_market/na_market[0]
##
##    # Plotting the prices with x-axis=timestamps
##    plt.clf()
##    plt.plot(ldt_timestamps, na_port_total, label='Portfolio')
##    plt.plot(ldt_timestamps, na_market, label='SPY')
##    plt.legend()
##    plt.ylabel('Returns')
##    plt.xlabel('Date')
##    plt.savefig('homework1.pdf', format='pdf')


