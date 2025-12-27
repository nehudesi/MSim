'''
Version: MRT v3.0
Type: module
Location: C:\MRT3.0\module
Author: Chintan Patel
Email: chintanlike@gmail.com

Bollinger Based Trading
'''


import pandas as pd
import numpy as np
#import math
import copy
import module.qsdateutil as du
import datetime as dt
import module.DataAccess as da
#import module.tsutil as tsu
#import module.EventProfiler as ep
from module import modDatesReturn
import csv
from module import basic


def find_events(ls_symbols, d_data):
    ''' Finding the event dataframe '''
    df_close = d_data['actual_close']
    # ts_market = df_close['SPY']

    print("Finding Events")

    # Creating an empty dataframe
    df_events = copy.deepcopy(df_close)
    df_events = df_events * np.NAN

    # Time stamps for the event range
    ldt_timestamps = df_close.index

    df_close = d_data['close']
    df_mean = pd.rolling_mean(d_data['close'], 20)
    df_std = pd.rolling_std(d_data['close'], 20)

    df_bollinger = (df_close - df_mean) / (df_std)
    writer = csv.writer(open('bollingerorders.csv', 'wb'), delimiter=',')
    
    f_symreturn_cutoff = input('<<< Enter the cutoff in decimel for symbol return today: ')
    f_symyest_cutoff = input('<<< Enter the cutoff in decimel for symbol return yesterday: ')
   
    print('1 -> SYMBOL_RETURN_TODAY > ', f_symreturn_cutoff, 'SYMBOL_RETURN_YESTERDAY < ',f_symyest_cutoff)
    print('2 -> SYMBOL_RETURN_TODAY < ', f_symreturn_cutoff, 'SYMBOL_RETURN_YESTERDAY > ',f_symyest_cutoff)
    print('3 -> SYMBOL_RETURN_TODAY > ', f_symreturn_cutoff, 'SYMBOL_RETURN_YESTERDAY > ',f_symyest_cutoff)
    print('4 -> SYMBOL_RETURN_TODAY <', f_symreturn_cutoff,  'SYMBOL_RETURN_YESTERDAY < ',f_symyest_cutoff)

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
            f_symboll_today = df_bollinger[s_sym].ix[ldt_timestamps[i]]
            f_symboll_yest = df_bollinger[s_sym].ix[ldt_timestamps[i - 1]]
            f_marketbol_today = df_bollinger['SPY'].ix[ldt_timestamps[i]]
            # f_marketprice_yest = ts_market.ix[ldt_timestamps[i - 1]]
            i_shares = 100
            
            if select == 1:
                if f_symboll_today > float(f_symreturn_cutoff) and f_symboll_yest < float(f_symyest_cutoff):
                    if f_marketbol_today > 1.0: 
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
                if f_symboll_today > float(f_symreturn_cutoff) and f_symboll_yest < float(f_symyest_cutoff):
                    if f_marketbol_today > 1.0:                    
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
                if f_symboll_today > float(f_symreturn_cutoff) and f_symboll_yest < float(f_symyest_cutoff):
                    if f_marketbol_today > 1.0:
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
                if f_symboll_today > float(f_symreturn_cutoff) and f_symboll_yest < float(f_symyest_cutoff):
                    if f_marketbol_today > 1.0:
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
            
            #if f_symboll_today < -2.0 and f_symboll_yest >= -2.0:
                #if f_marketbol_today > 1.0:
                    #df_events[s_sym].ix[ldt_timestamps[i]] = 1
                    #row_to_enter = [str(ldt_timestamps[i].year), str(ldt_timestamps[i].month), \
                            #str(ldt_timestamps[i].day), s_sym, 'Buy', i_shares]
                    #writer.writerow(row_to_enter)
                    #try:
                        #time_n = ldt_timestamps[i + 5]
                    #except:
                        #time_n = ldt_timestamps[-1]
                    #row_to_enter = [str(time_n.year), str(time_n.month), \
                            #str(time_n.day), s_sym, 'Sell', i_shares]
                    #writer.writerow(row_to_enter)

    return df_events


def eventBollingerMain():
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

    find_events(ls_symbols, d_data)

    # print("Creating Study"
    # ep.eventprofiler(df_events, d_data, i_lookback=20, i_lookforward=20,
    #             s_filename='MyEventStudy.pdf', b_market_neutral=True, b_errorbars=True,
    #             s_market_sym='SPY')