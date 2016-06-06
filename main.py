"""
MARKET RESEARCH TOOL
Version : v3.0
Location: C:\MRT3.0
@author: Chintan patel
@Email: chintanlike@gmail.com

"""

import os
#import time
from module.basic import *

#from module.analyze import *
from module.yahooDataPull import yahooDatamain
#from module.eventmod import *
#from module.marketsim import *
from module.usrHelp import usrHelpMain
from module.generalCalc import generalcalc
#from module.portAnalyzer import *
from module.researchstock import researchstockMain
from module.fundAnalysis import fundanalysisMain

def print_logo():
    os.system("CLS")
    print ' #################################################################################################'
    print '\t\t\t                MARKET RESEARCH TOOL '
    print '\t\t\t                       BASIC '
    print '\t\t\t                       v3.0 '
    print ' #################################################################################################\n'


def print_symbol_file():
    symbol_file = os.path.join(os.getcwd(),'MRT_SYMBOLS.txt')
    f = open(symbol_file,'r')
    contents = f.read()
    print "### Current symbols files has below symbols..###"
    print (contents)

def main():
    cont = 1
    while cont != 0:
        print_logo()
        print '\t\t\t                <<< Main Menu >>> \n'
        print '\t [1] Load Data/Update  [2] General Calculations   [3] Fund Analysis '
        print '\t [4] Stock Research    [7] Help                   [8] Exit'
            
        try:
            sel = input('\n<<< Select: ')
        except SyntaxError:                             
            print '<<<(w) Invalid Entry'
            time.sleep(2)
            main()
        except NameError:                             
            print '<<<(w) Invalid Entry'
            time.sleep(2)                              
            main()
        except ValueError:                          
            print '<<<(w) Invalid Entry'
            time.sleep(2)
            main()
            
        try:
            if sel == 1:
                print_logo()
                print '\t\t\t             <<< Load Data/Update >>> \n '
                print "<<<(i) Update MRT_SYMBOLS.txt file with specific symbols list in it "
                print_symbol_file()
                s = str(raw_input("<<<(i) Press Y if created or else N: "))
                if s == 'Y' or s == 'y':
                    yahooDatamain()
                else:
                    print '<<<(s) Update MRT_SYMBOLS.txt.. >>>'
                    time.sleep(2)
                    continue
            elif sel == 2:
                print_logo()
                generalcalc()
            elif sel == 3:
                print_logo()
                fundanalysisMain()
            elif sel == 4:
                print_logo()
                researchstockMain()                                                                                               
            elif sel == 7:
                print_logo()
                usrHelpMain()
            elif sel == 8:
                exit(0)
            else:
                print_clrscr()
                main()
            
        except SyntaxError:
            print '<<<(w) Oops..Invalid Selection >>>'
            print_clrscr()
            main()
        except ValueError:
            print '<<<(w) Oops..Invalid Selection >>>'
            print_clrscr()
            main() 
                             
        print ' ------------------------------------------------------------------------------------------------ '
        try:
            cont = input('<<<(i) Press 0 to exit simulator..: ')
            os.system('CLS')
        except NameError:
            print '<<<(w) Oops..Invalid Selection >>>'
            print_clrscr()
            main()
        except SyntaxError:
            print '<<<(w) Oops..Invalid Selection >>>'
            time.sleep(2)
            main()
            
if __name__ == '__main__':
    
    disclaimer()
    sel = str(raw_input('I Agree(Y/N): '))
    if sel == 'Y' or sel == 'y':
        main()
    else:
        print '<<(w) You must Agree with Software terms to use this softwrae..\n'
        time.sleep(5)
        exit(0)
    
