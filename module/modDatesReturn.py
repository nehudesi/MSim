'''
Version: MRT v3.0
Type: module
Location: C:\MRT3.0\module
Author: Chintan Patel
Email: chintanlike@gmail.com
'''

import basic
import datetime

def get_dates():
        print '------------------------------------------------------------- '
        try:
                start_month = int(input('<<< Enter Start Month: '))
            
                if int(start_month) > 12 or int(start_month) <= 0:
                        basic.print_clrscr()
                        basic.go_back()
                        
                start_day = int(input('<<< Enter Start Day: '))
                if int(start_day) > 31 or int(start_day) <= 0:
                        basic.print_clrscr()
                        basic.go_back()

                start_year = int(input('<<< Enter Start Year: '))
                now = datetime.datetime.now()
                if int(start_year) > now.year or int(start_year) < 2010:
                        basic.print_clrscr()
                        basic.go_back()
    
                end_month = input('<<< Enter End Month: ')
                if int(end_month) > 12 or int(end_month) <= 0:
                        basic.print_clrscr()
                        basic.go_back()
                        
                end_day = input('<<< Enter End Day: ')
                if int(end_day) > 31 or int(end_day ) <= 0:
                        basic.print_clrscr()
                        basic.go_back()
                        
                end_year = input('<<< Enter End Year: ')
                if int(end_year) > now.year or int(end_year) < 2010:
                        basic.print_clrscr()
                        basic.go_back()
                        
                if start_year > end_year:
                    print '<<<(w)End Year should be greater than start year'
                    basic.print_clrscr()
                    basic.go_back()
            
        except ValueError:
                basic.print_clrscr()
                basic.go_back()

        except SyntaxError:
                basic.print_clrscr()
                basic.go_back()
        except NameError:
                basic.print_clrscr()
                basic.go_back()
        
        leap_year_start = start_year%4 
        leap_year_end = end_year%4
        
        if leap_year_start != 0 or leap_year_end != 0:
            if start_day == 29 or end_day == 29:
                print '<<(w) Not leap year..\n' 
                basic.print_clrscr()
                basic.go_back()
                        
        
        return start_month,start_day,start_year,end_month,end_day,end_year