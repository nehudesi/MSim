'''
Version: MRT v3.0
Type: module
Location: C:\MRT3.0\module
Author: Chintan Patel
Email: chintanlike@gmail.com

'''

import os
import time




def print_logo():
    os.system("CLS")
    print(' #################################################################################################')
    print('\t\t\t                MARKET RESEARCH TOOL ')
    print('\t\t\t                       BASIC ')
    print('\t\t\t                       v3.0 ')
    print(' #################################################################################################\n')

def print_clrscr():
    print('<<<(w) Invalid Entry')
    time.sleep(2)

def go_back():
    print('<<<(i) Going Back..')
    time.sleep(2)
    import main
    main.main()

def get_num_sym():
    try:
        len_sym = int(input('<<< How many symbols: '))
        if len_sym < 25 and len_sym >= 1:
            pass
        elif len_sym == 0:
            print('Please enter value greater than <0>...\n')
            print_clrscr()
            print_logo()
            import main
            main.main()
        else:
            while len_sym > 25:
                print("<<<(w) Invalid Value: <Enter Value less than 25>")
                len_sym = int(input('<<< How many symbols: '))
                
    except ValueError:
        print("<<<(w) Oops!  That was no valid number.  Try again...")
        print_clrscr()
        print_logo()            
        import main
        main.main()
  
    except SyntaxError:
        print("<<<(w) Oops!  That was no valid number.  Try again...")
        print_clrscr()
        print_logo()
        import main
        main.main()
  
    except NameError:
        print("<<<(w) Oops!  That was no valid number.  Try again...")
        print_clrscr()
        print_logo()
        import main
        main.main()
          
    return len_sym

def disclaimer():
    print('###############################################################################')
    print('\t\t                MARKET RESEARCH TOOL ')
    print('\t\t                       BASIC ')
    print('\t\t                       v3.0 ')
    print('###############################################################################\n')
    print('Copyrights@ Chintan Patel\n')
    print('--------------------------------------------------------------------------------------------------\n')
    declaration = ''' 
    This Software is the property of Chintan Patel and may not be copied in
    any form without the expressed permission of author. It is entrusted
    to the customers of Chintan Patel for their information only. The
    information contained herein is proprietary and confidential and may  not
    be  transferred,transported,  or transmitted  by any means without the
    expressed permission of author. Author  makes  no  guarantee
    to the completeness or the correctness of  the  information  contained in
    this  document and retains the right to make changes at any time, without
    notice.
    '''
    print(declaration.center(50, ' '))
    
#     print('This Software is the property of Chintan Patel and may not be copied in any form without' 
#     print('the expressed permission of Chintan Patel. It is entrusted to the customers of Chintan Patel'
#     print('for their information only. The information contained herein is proprietary and'
#     print('confidential and may not be transferred, transported, or transmitted by any means' 
#     print('without the expressed permission of Chintan Patel. Chintan Patel makes no guarantee to the'
#     print('completeness or the correctness of the information contained in this document and'
#     print('retains the right to make changes at any time, without notice.\n'
#     print('---------------------------------------------------------------------------------------------------'
    
          
def checkDemodate():
    from datetime import datetime
    #Set Expired Date          
    expired_date = datetime(2017,12,30) #YYYMMDD
    present_date = datetime.now()
          
    if expired_date > present_date:
        pass
    else:
        print(' <<<(w) Your Software is Expired.\n')
        print(' <<<(i) Please contact Owner for details.')
        time.sleep(2)
        exit(0)