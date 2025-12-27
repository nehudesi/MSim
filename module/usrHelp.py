'''
Version: MRT v3.0
Type: module
Location: C:\MRT3.0\module
Author: Chintan Patel
Email: chintanlike@gmail.com

'''
from module import basic

def help_yahooDataPull():
    print('----------------------------------- Load Data/Update ------------------------------------------ ')
    str1 = ''' 
    Help to load latest data from finance.yahoo.com 
    Create MRT_SYMBOLS.txt file in same folder with symbols to be loaded.  
    This   will  load  data  from  January  01,  2010 to  present  day.
    Please contact author to load data from different date. 
    Loaded files for all symbols would be available at C:\MRT3.0\Data\Yahoo'           
    To load Market files ex: SPX, DOW, write symbol name staring with "$":ex: $SPY
    '''
    print(str1.center(20, ' '))
    del str1
    
def help_generalCalc():
    print('-------------------------------- General Calculations -----------------------------------------')
    str1 = '''
    Useful for daily calculations.
    Enter the date for considering Stock value to count.        
    1. Plot Adjusted Close
    >> Plot the graph for entered symbols.(Max: Symbol = 25).
    Enter the symbol for stocks; not case sensitive. Calculation is based on 
    daily adjusted prices of stock. 
    2. Calculate Daily Return
    >> Calculates daily return for entered stocks. Calculates for adjusted prices.
    '3. Calculate Standard Devation
    >> Calculates Devation for entered symbols symbols
    4. Optimized Portfolio
    >> Optimized portfolio for symbols based on returns. Prints Max, Min Weight of portfolio.
    5. Get Sharpe Ration
    >> Calculates sharpe ratio for particular symbols.
    '''
    print(str1.center(20, ' '))
    del str1
          

def help_portfolioanalyzer():
    print('----------------------------- Analyze Portfolio Allocation -----------------------------------')
    str1 = '''
    Create  portfolioanalyze.csv  file  with  symbol allocation in the form of 
    fraction [0.0 - 0.1].
    Based on allocation from portfolioanalyze.csv, and past values of adjusted 
    daily  return  a plot with estimated return is created for that allocation'
    '''
    print(str1.center(20, ' '))
    del str1
def help_eventanalyzer():
    print('----------------------------- Event Analyzer -------------------------------------------------')
    str1 = '''
    Based on Adjusted close value for  symbols plot will be created to understand the event.
    Event may be market fall  for some  percentage and symbol rise/fall for some percentage.
    Update the  file mrtevent  with  symbols of  interested  on  which  event  is  analyzed
    A pdf file would be created after runnning this options with shows events generated based
    on your demand.'
    If there is no event it will not generate any pdf file.
    orders.csv is created to plan a strategy which can be feed in analyzing portfolio. Based on
    orders.csv will of Buy and sell format.
    Above is applied to Bollinger based event also except there would not any pdf file
    <<< Default market is SPY >>>
    '''
    print(str1.center(20, ' '))
    del str1

def help_analyzPort():
    print('------------------------------ Analyze Portfolio --------------------------------------------')
    str1 = '''
    Update orders.csv for you past order.
    Based on entered cash, analysis will be done for that trading.
    Enter Benchmark starting with $ for comparision your fund
    File <values.csv> will be updated for funds value on every day
    Plot will be created Fund vs Benchmark. You will get options to generate report
    <<< Default market is SPY >>>
    '''
    print(str1.center(20, ' '))
    del str1

def help_fundAnalysis():
    help_portfolioanalyzer()
    help_eventanalyzer()
    help_analyzPort()
                    
def help_researchStock():
    print('------------------------------- Stock Research ------------------------------------------------')
    str1 = '''
    This option gives an oppurtunity to research individual stock.
    1. Bollinger Plot 
    Draw Bollinger Plot with providing individual stock symbol
    3. Scattered Plots
    Used to plot scattered plots to compare two stocks.
    <<< Default market is SPY >>>
    '''
    print(str1.center(20, ' '))
    del str1

def help_about():
        print('---------------------------------- About ---------------------------------------------------')
        str1 = '''
        Author of this software is Chintan Patel. For any further info
        contact  author.  Author  does  not  Guarantee  for  any  info
        provided by this software.
        @Author: Chintan Patel; chintanlike@gmail.com
        '''
        print(str1.center(20, ' '))
        del str1
                        
def usrHelpMain():
    print('\t\t\t             <<< Help >>> \n ')
    print('\t [1] Load Data             [2] General Calculations    [3] Fund Analysis')
    print('\t [4] Reserach Stock        [5] About                   [7] Main Menu')

    try:
        sel = int(input('Select: '))

    except (SyntaxError, ValueError, NameError):
        basic.print_clrscr()
        basic.go_back()

    if sel == 1:
        help_yahooDataPull()
    elif sel == 2:
        help_generalCalc()                   
    elif sel == 3:
        help_fundAnalysis()     
    elif sel == 4:
        help_researchStock()
    elif sel == 5:
        help_about()                    
    elif sel == 7:
        basic.go_back()                    
    else:
        basic.print_clrscr()
        basic.go_back()
                    
          
