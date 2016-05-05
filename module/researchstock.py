"""
Version: MRT v3.0
Type: module
Location: C:\MRT3.0\module
Author: Chintan Patel
Email: chintanlike@gmail.com
    
"""

import bollingerPlot
from generalCalc import *
#import basic




def scatterplot():
    # Plotting the scatter plot of daily returns between XOM VS $SPX
    objcalc = GeneralCalc()
    #sym = list()        
    sym = objcalc.ls_symbols
    if len(sym) > 2:
        print '<<<(w) Invalid Number..\n'
        print '<<<(i) Please enter 2 symbols only..\n'
        basic.print_clrscr()
        basic.print_logo()        
        researchstockMain()
        
    rets = objcalc.calDailyReturn()    
    
    plt.clf()
    plt.scatter(rets[:, 0],rets[:, 1],c='blue')
    plt.ylabel(sym[0])
    plt.xlabel(sym[1])
    plt.savefig('scatter.pdf', format='pdf')
    plt.grid(axis='both')
    plt.show()

def researchstockMain():
    print '\t\t\t                <<< Research Stock >>> \n '
    print '\t [1] Bollinger Plot   [2] Calculate Book Value   [3] Scattered Plot  '
    print '\t [7] Main Menu'  
    
    try:
        sel_opt = input('\n<<< Select: ')
    except SyntaxError:
        basic.print_clrscr()
        basic.print_logo()
        researchstockMain()
    except NameError:
        basic.print_clrscr()
        basic.print_logo()
        researchstockMain()
    except ValueError:
        basic.print_clrscr()
        basic.print_logo()
        researchstockMain()
    
    if sel_opt == 1:
        bollingerPlot.bollingerplotMain()
    elif sel_opt == 3:
        print '<<<(i) Please enter 2 symbols only..\n'
        scatterplot()       
    elif sel_opt == 7:
        basic.go_back()     
    else:
        basic.print_clrscr()
        basic.print_logo()
        researchstockMain()        