'''
Version: MRT v3.0
Type: module
Location: C:\MRT3.0\module
Author: Chintan Patel
Email: chintanlike@gmail.com
'''

import module.tsutil as tsu
import module.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
from pylab import *
#import sys
import pandas
import csv
#import report
import basic
from copy import deepcopy
import scipy.stats as scst

def _csv_read_fund(filename):
    reader = csv.reader(open(filename, 'rU'), delimiter=',')
    vals = []
    dates = []
    for row in reader:
        vals.append(float(row[3]))
        date = dt.datetime(int(row[0]), int(row[1]), int(row[2]), 16)
        dates.append(date)
    ts_fund = pandas.TimeSeries(dict(zip(dates, vals)))
    return ts_fund


def _read_bench(symbol, timestamps):

    dataobj = da.DataAccess('Yahoo')
    close = dataobj.get_data(timestamps, [symbol], "close", verbose=True)
    close = close.fillna(method='ffill')
    close = close.fillna(method='bfill')
    return close[symbol]

def ks_statistic(ts_fund):
    fund_ts = deepcopy(ts_fund)
    if len(fund_ts.values) > 60:
        seq1 = fund_ts.values[0:-60]
        seq2 = fund_ts.values[-60:]
        tsu.returnize0(seq1)
        tsu.returnize0(seq2)
        (ks, p) = scst.ks_2samp(seq1, seq2)
        return ks, p
    # elif len(fund_ts.values) > 5:
    #     seq1 = fund_ts.values[0:-5]
    #     seq2 = fund_ts.values[-5:]
    #     (ks, p) = scst.ks_2samp(seq1, seq2)
    #     return ks, p

    ks = -1
    p = -1
    return ks, p



def analyzeMain():
    ts_fund = _csv_read_fund('values.csv')
    try:
        benchmark = raw_input('Enter Benchmark: ')
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


    bench_vals = _read_bench(benchmark, list(ts_fund.index))
    # print(bench_vals))
    multiple = ts_fund[0] / bench_vals[0]
    bench_vals = bench_vals * multiple
    
    print("Details of the Performance of the portfolio"
    print("Total Fund:", ts_fund[0]
    print('Data Range : ', ts_fund.index[0], ' to ', ts_fund.index[-1]
    print('Sharpe Ratio of Fund :', tsu.get_sharpe_ratio(tsu.daily(ts_fund)[0]
    print('Sharpe Ratio of ' + benchmark + ' :', tsu.get_sharpe_ratio(
                                              tsu.daily(bench_vals))[0]
    print('Total Return of Fund : ', (((ts_fund[-1] / ts_fund[0]) - 1) + 1)
    print('Total Return of ' + benchmark + ' :', (((bench_vals[-1]
                                                / bench_vals[0]) - 1) + 1)
    print('Standard Deviation of Fund : ', np.std(tsu.daily(
                                           ts_fund.values))
    print('Standard Deviation of ' + benchmark + ' :', np.std(
                                           tsu.daily(bench_vals.values))

    print('Average Daily Return of Fund : ', np.mean(tsu.daily(
                                           ts_fund.values))
    print('Average Daily Return of ' + benchmark + ' :', np.mean(
                                           tsu.daily(bench_vals.values))
    KS, P = ks_statistic(ts_fund)    
    print("KS P:" , KS,P    
    plt.clf()
    plt.plot(ts_fund.index, ts_fund.values)
    plt.plot(ts_fund.index, bench_vals)
    plt.ylabel('Fund Value', size='xx-small')
    plt.xlabel('Date', size='xx-small')
    plt.legend(['Fund', 'Benchmark'], loc='best')
    plt.xticks(size='xx-small')
    plt.yticks(size='xx-small')
    plt.grid(axis='both')
    plt.show()
    savefig('funds.png', format = 'png')
    
    try:
        report = input("Want to generate report(Press 1): ")
        
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
        
    if report == 1:
        name = str(dt.datetime.now())
        file_conv = name.replace(" ", "")
        file_conv1 = file_conv.replace(":","_")
        file_conv2 = file_conv1.replace("-","_")
        filename = file_conv2+".html"
        print('Generating report..', filename
        html_file  =  open(filename,"w+")
        html_file.write("<HTML>\n")
        html_file.write("<HEAD>\n")
        html_file.write("<TITLE>MSim Generated Report:" + name + "</TITLE>\n")    
        html_file.write("<H1>Details of the Performance of the portfolio</H1>")
        html_file.write("</HEAD>\n\n")
        html_file.write("<BODY>\n\n")
        html_file.write("<IMG SRC = \'./funds.png\' title=Funds vs Benchmark align=right height= 500 width = 600/>\n")
        html_file.write("<p><i> Total Fund:" +str(ts_fund[0])+ "</p\n")        
        html_file.write("<p><i>Data Range : </i>," +str(ts_fund.index[0])+ "to ," +str(ts_fund.index[-1])+"</p\n")
        html_file.write("<p><i>Sharpe Ratio of Fund :</i>"+str(tsu.get_sharpe_ratio(tsu.daily(ts_fund))[0])+"</p\n")
        html_file.write("<p><i>Sharpe Ratio of </i>" + benchmark + ":" +str(tsu.get_sharpe_ratio(tsu.daily(bench_vals))[0])+"</p\n")

        html_file.write("<p><i>Sharpe Ratio of Fund : ,</i>" +str(tsu.get_sharpe_ratio(tsu.daily(ts_fund))[0])+"</p\n")
        html_file.write("<p><i>Sharpe Ratio of </i>" + benchmark + ":" +str(tsu.get_sharpe_ratio(tsu.daily(bench_vals))[0])+"</p\n")
        html_file.write("<p><i>Total Return of Fund :</i>" +str((((ts_fund[-1] / ts_fund[0]) - 1) + 1))+"</p\n")
        html_file.write("<p><i>Total Return of </i>" + benchmark + " : " +str((((bench_vals[-1]/ bench_vals[0]) - 1) + 1))+"</p\n")
        html_file.write("<p><i>Standard Deviation of Fund : </i>" +str(np.std(tsu.daily(ts_fund.values)))+"</p\n")
        html_file.write("<p><i>Standard Deviation of </i>"+ benchmark + ":" +str(np.std(tsu.daily(bench_vals.values)))+"</p\n")
    
        html_file.write("<p><i>Average Daily Return of Fund : </i> " +str(np.mean(tsu.daily(ts_fund.values)))+"</p\n")
        html_file.write("<p><i>Average Daily Return of </i>" + benchmark + " : " + str(np.mean(tsu.daily(bench_vals.values)))+"</p\n")
        html_file.write("<link type=text/csv rel=stylesheet href=D:\Sim\MSimv2.1/orders.csv />")

        html_file.write("</BODY>\n\n")
        html_file.write("</HTML>")    