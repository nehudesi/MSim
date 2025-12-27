'''
Version: MRT v3.0
Type: module
Location: C:\MRT3.0\module
Author: Chintan Patel
Email: chintanlike@gmail.com

Generate Event for Specific Symbol and Dates
'''
import module.qsdateutil as du
import module.DataAccess as da
#import module.tsutil as tsu
import module.EventProfiler as ep

#import pandas as pd
import numpy as np
#import math
import copy
import csv
from module import basic
from module import modDatesReturn
from module import eventBollinger
import datetime as dt

def find_events(ls_symbols, d_data):
    ''' Finding the event dataframe '''
    df_close = d_data['actual_close']
    ts_market = df_close['SPY']

    print("Finding Events")

    # Creating an empty dataframe
    df_events = copy.deepcopy(df_close)
    df_events = df_events * np.NAN
    # Time stamps for the event range
    ldt_timestamps = df_close.index
    writer = csv.writer(open('orders.csv', 'wb'), delimiter=',')
    
    f_symreturn_cutoff = float(input('<<< Enter the cutoff in decimel for symbol return today: '))
    f_marketreturn_cutoff = float(input('<<< Enter the cutoiff in decimel for market return today: '))
    print('1 -> SYMBOL_RETURN_TODAY > ', f_symreturn_cutoff, ' & MARKET_RETURN_TODAY  < ', f_marketreturn_cutoff)
    print('2 -> SYMBOL_RETURN_TODAY < ', f_symreturn_cutoff, ' & MARKET_RETURN_TODAY  > ', f_marketreturn_cutoff)
    print('3 -> SYMBOL_RETURN_TODAY > ', f_symreturn_cutoff, ' & MARKET_RETURN_TODAY  > ', f_marketreturn_cutoff)
    print('4 -> SYMBOL_RETURN_TODAY <', f_symreturn_cutoff, ' & MARKET_RETURN_TODAY  < ', f_marketreturn_cutoff)
    
    try:
        select = input('Select: ')
    except ValueError:
            basic.print_clrscr()
            basic.print_logo()
            basic.go_back()
    except SyntaxError:
            basic.print_clrscr()
            basic.print_logo()
            basic.go_back()
    except NameError:
            basic.print_clrscr()
            basic.print_logo()
            basic.go_back()


    for s_sym in ls_symbols:
        for i in range(1, len(ldt_timestamps)):
            # Calculating the returns for this timestamp
            f_symprice_today = df_close[s_sym].ix[ldt_timestamps[i]]
            f_symprice_yest = df_close[s_sym].ix[ldt_timestamps[i - 1]]
            f_marketprice_today = ts_market.ix[ldt_timestamps[i]]
            f_marketprice_yest = ts_market.ix[ldt_timestamps[i - 1]]
            f_symreturn_today = (f_symprice_today / f_symprice_yest) - 1

            f_marketreturn_today = (f_marketprice_today / f_marketprice_yest) - 1
            i_shares = 100
            
            if select == 1:
                if f_symreturn_today > float(f_symreturn_cutoff) and f_marketreturn_today < float(f_marketreturn_cutoff):
                    df_events[s_sym].ix[ldt_timestamps[i]] = 1
                    row_to_enter = [str(ldt_timestamps[i].year), str(ldt_timestamps[i].month), \
                                            str(ldt_timestamps[i].day), s_sym, 'Buy', i_shares]
                    writer.writerow(row_to_enter)
                    try:
                        time_n = ldt_timestamps[i + 5]
                    except:
                        time_n = ldt_timestamps[-1]
                    row_to_enter = [str(time_n.year), str(time_n.month), \
                                            str(time_n.day), s_sym, 'Sell', i_shares]
                    writer.writerow(row_to_enter)   
                        
            elif select == 2:
                if f_symreturn_today < float(f_symreturn_cutoff) and f_marketreturn_today > float(f_marketreturn_cutoff):
                    df_events[s_sym].ix[ldt_timestamps[i]] = 1
                    row_to_enter = [str(ldt_timestamps[i].year), str(ldt_timestamps[i].month), \
                                            str(ldt_timestamps[i].day), s_sym, 'Buy', i_shares]
                    writer.writerow(row_to_enter)
                    try:
                        time_n = ldt_timestamps[i + 5]
                    except:
                        time_n = ldt_timestamps[-1]
                    row_to_enter = [str(time_n.year), str(time_n.month), \
                                            str(time_n.day), s_sym, 'Sell', i_shares]
                    writer.writerow(row_to_enter)                    
            
            elif select == 3:
                if f_symreturn_today > float(f_symreturn_cutoff) and f_marketreturn_today > float(f_marketreturn_cutoff):
                    df_events[s_sym].ix[ldt_timestamps[i]] = 1
                    row_to_enter = [str(ldt_timestamps[i].year), str(ldt_timestamps[i].month), \
                                            str(ldt_timestamps[i].day), s_sym, 'Buy', i_shares]
                    writer.writerow(row_to_enter)
                    try:
                        time_n = ldt_timestamps[i + 5]
                    except:
                        time_n = ldt_timestamps[-1]
                    row_to_enter = [str(time_n.year), str(time_n.month), \
                                            str(time_n.day), s_sym, 'Sell', i_shares]
                    writer.writerow(row_to_enter)
                        
            else:
                if f_symreturn_today < float(f_symreturn_cutoff) and f_marketreturn_today < float(f_marketreturn_cutoff):
                    df_events[s_sym].ix[ldt_timestamps[i]] = 1
                    row_to_enter = [str(ldt_timestamps[i].year), str(ldt_timestamps[i].month), \
                                            str(ldt_timestamps[i].day), s_sym, 'Buy', i_shares]
                    writer.writerow(row_to_enter)
                    try:
                        time_n = ldt_timestamps[i + 5]
                    except:
                        time_n = ldt_timestamps[-1]
                        row_to_enter = [str(time_n.year), str(time_n.month), \
                                            str(time_n.day), s_sym, 'Sell', i_shares]
                        writer.writerow(row_to_enter)                    
                
    return df_events


def eventmodMain():
    start_month,start_day,start_year,end_month,end_day,end_year = modDatesReturn.get_dates()    
    dt_start = dt.datetime(start_year, start_month, start_day)
    dt_end = dt.datetime(end_year, end_month, end_day)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_symbols = dataobj.get_symbols_from_list('mrtevent')
    ls_symbols.append('SPY')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    for s_key in ls_keys:
        d_data[s_key] = d_data[s_key].fillna(method = 'ffill')
        d_data[s_key] = d_data[s_key].fillna(method = 'bfill')
        d_data[s_key] = d_data[s_key].fillna(1.0)

    df_events = find_events(ls_symbols, d_data)
    print("Creating Study")
    ret = ep.eventprofiler(df_events, d_data, i_lookback=20, i_lookforward=20,
                s_filename='MyEventStudy.pdf', b_market_neutral=True, b_errorbars=True,
                s_market_sym='SPY')
    
    if ret == 0:
        print('No events')
        basic.print_clrscr()
        basic.print_logo()
        eventmenuMain()
        
def eventmenuMain():
    
    print('\t\t\t             <<< Event Analyzer >>> \n ')
    print(' [1] Event based on Market           [2] Event based on Bollinger')
    print(' [7] Main Menu ')

    try:
        sel_opt = input('\n<<< Select: ')
    except SyntaxError:
        basic.print_clrscr()
        basic.print_logo()
        eventmenuMain()
    except NameError:
        basic.print_clrscr()
        basic.print_logo()
        eventmenuMain()
 
    if sel_opt == 1:
        eventmodMain()
    elif sel_opt == 2:
        eventBollinger.eventBollingerMain()
    elif sel_opt == 7:
        basic.go_back()
    else:
        basic.print_clrscr()
        basic.print_logo()
        eventmenuMain()
        

    
    