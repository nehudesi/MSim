"""
Version: MRT v3.0
Type: module
Location: C:\MRT3.0\module
Author: Chintan Patel
Email: chintanlike@gmail.com

This module print(daily return, sharpe ratios, stddev, and graphs))
Select appropriate choice
"""

# QSTK Imports
import module.qsdateutil as du
import module.tsutil as tsu
import module.DataAccess as da

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
#import pandas as pd
import numpy as np
from module import basic
from module import bestPortfolio
import csv
from module import modDatesReturn

class GeneralCalc(object):
    def __init__(self):
        # List of symbols

        self.ls_symbols = list()
        
        

        len_sym = basic.get_num_sym()
            
        for i in range(len_sym):
            symbols = str(input('<<< Enter symbols:' ))
            self.ls_symbols.append(symbols)
                
             

        start_month,start_day,start_year,end_month,end_day,end_year = modDatesReturn.get_dates()    
        dt_start = dt.datetime(start_year, start_month, start_day)
        dt_end = dt.datetime(end_year, end_month, end_day)

        # We need closing prices so the timestamp should be hours=16.
        dt_timeofday = dt.timedelta(hours=16)

        # Get a list of trading days between the start and the end.
        self.ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

        # Creating an object of the dataaccess class with Yahoo as the source.
        c_dataobj = da.DataAccess('Yahoo')

        # Keys to be read from the data, it is good to read everything in one go.
        ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']

        # Reading the data, now d_data is a dictionary with the keys above.
        # Timestamps and symbols are the ones that were specified before.
        ldf_data = c_dataobj.get_data(self.ldt_timestamps, self.ls_symbols, ls_keys)
        self.d_data = dict(zip(ls_keys, ldf_data))

        # Getting the numpy ndarray of close prices.
        self.na_price = self.d_data['close'].values
        
    def plotAdjustedClose(self):
        # Plotting the prices with x-axis=timestamps
        plt.clf()
        plt.plot(self.ldt_timestamps, self.na_price)
        plt.legend(self.ls_symbols)
        plt.ylabel('Adjusted Close')
        plt.xlabel('Date')
        plt.grid(axis='both')
        plt.show()

    def calDailyReturn(self):

        # Normalizing the prices to start at 1 and see relative returns

        na_normalized_price = self.na_price / self.na_price[0, :]

    
        # Copy the normalized prices to a new ndarry to find returns.
        na_rets = na_normalized_price.copy()

        # Calculate the daily returns of the prices. (Inplace calculation)
        # returnize0 works on ndarray and not dataframes.
        tsu.returnize0(na_rets)
        
        log = int(input('<<< 1. Dump data in to file .. \n<<< 2. Print on console\n<<< 0. Press 0 to ignore: '))

        #open log file
        if log == 1:
            writer =  csv.writer(open('daliy_returns.csv','w'),delimiter=',')
            
            writer.writerow(self.ls_symbols)
            
            row = list()
            writer =  csv.writer(open('daliy_returns.csv','a'),delimiter='\n')
            for i in range(len(self.ldt_timestamps)):
                    row.append(str(self.ldt_timestamps[i]) + str(na_rets[i] * 100))
            
            writer.writerow(row)
            #log_file=open("daily_returns.txt","w")
            #log_file.write("Daily Return,\n")
            #for i in range(len(self.ls_symbols)):
            #log_file.write(str(self.ls_symbols[i]))

            #log_file.write("\n")
            #log_file.write(str(na_rets * 100))
            #log_file.close()

        #write column headings
        
        print()
        if log == 2:
            print(' Date ', '\t\t')

            for i in range(len(self.ls_symbols)):
                print('\t\t', self.ls_symbols[i])

            for i in range(len(self.ldt_timestamps)):
                print(self.ldt_timestamps[i],'\t', na_rets[i] * 100,'\n')
         
        if log == 0:
            return na_rets
        # Plotting the prices with x-axis=timestamps
        plt.clf()
        plt.plot(self.ldt_timestamps, na_rets)
        plt.legend(self.ls_symbols)
        plt.ylabel('Daily Return')
        plt.xlabel('Date')
        plt.grid(axis='both')
        plt.show()
                
        return na_rets

     
    def calStdDev(self,ret_daily):
        
        std_dev = np.std(ret_daily)
        print('<<< Standard Deviation:',std_dev*100,'%')
        
    def getPortfolioOpt(self, rets):
        basic.print_clrscr()
        basic.print_logo()        
        #l_period = input('<<< Enter period to compress return i.e 7 = Weekly : ')
        f_target = float(input('<<< Target Return: '))
        na_lower = np.zeros(rets.shape[1])
        na_upper = np.ones(rets.shape[1])
        
        weight_port,min_ret, max_ret = tsu.OptPort(rets, f_target, na_lower, na_upper,s_type="long")
        print("<<< Weight of Portfolio:", weight_port)
        print("<<< Error:", max_ret)
        print("<<< Minimum Return:", min_ret)

    def getSharpeRatio(self, rets):
        sharpe_ratio = tsu.get_sharpe_ratio(rets)
        print('<<< Sharpe Ration:', sharpe_ratio)

        
def generalcalc():
    print('\t\t\t                <<< General Calculations >>> \n ')
    print(' [1] Plot Adjusted Close      [2] Calculate Daily Return  [3] Calculate Standard Devation')
    print(' [4] Optimized Portfolio      [5] Get Sharpe Ration       [6] Best Portfolio')
    print(' [7] Main Menu ')

    try:
        sel_opt = int(input('\n<<< Select: '))
    except (SyntaxError, NameError, ValueError):
        basic.print_clrscr()
        basic.print_logo()
        generalcalc()

    if sel_opt == 1:
        objcalc = GeneralCalc()
        objcalc.plotAdjustedClose()
    elif sel_opt == 2:
        objcalc = GeneralCalc()
        objcalc.calDailyReturn()
    elif sel_opt == 3:
        objcalc = GeneralCalc()
        d_ret = objcalc.calDailyReturn()
        objcalc.calStdDev(d_ret)
    elif sel_opt == 4:
        objcalc = GeneralCalc()
        rets = objcalc.calDailyReturn()
        objcalc.getPortfolioOpt(rets)
    elif sel_opt == 5:
        objcalc = GeneralCalc()
        rets = objcalc.calDailyReturn()
        objcalc.getSharpeRatio(rets)
    elif sel_opt == 6:
        bestPortfolio.bestPort()
    elif sel_opt == 7:
        basic.go_back()
    else:
        basic.print_clrscr()
        basic.print_logo()
        generalcalc()
        
        

