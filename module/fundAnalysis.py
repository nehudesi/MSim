'''
Version: MRT v3.0
Type: module
Location: C:\MRT3.0\module
Author: Chintan Patel
Email: chintanlike@gmail.com

'''

from module import basic

from module.eventmod import eventmenuMain
from module.marketsim import marketsimMain
#from analyze import *
from module.portAnalyzer import portfolioAnalyz





def fundanalysisMain():

    print('\t\t\t                <<< Fund Analysis >>> \n')
    print('\t [1] Analyze Portfolio Allocation  [2] Event Analyzer    [3] Analyze Portfolio')  
    print('\t [7] Main Menu ')
    
    try:
        sel_opt = int(input('\n<<< Select: '))
    except (SyntaxError, NameError, ValueError):
        basic.print_clrscr()
        basic.print_logo()
        fundanalysisMain()
        
    if sel_opt == 1:
        basic.print_logo()
        portfolioAnalyz()
    elif sel_opt == 2:
        basic.print_logo()
        eventmenuMain()
    elif sel_opt  == 3:
        basic.print_logo()
        print('<<<(s) Update orders.csv file.. \n')
        marketsimMain()
    elif sel_opt == 7:
        basic.go_back()
    else:
        basic.print_clrscr()
        basic.print_logo()
        fundanalysisMain()