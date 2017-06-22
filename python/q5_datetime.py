# Hint:  use Google to find python function

from datetime import datetime

####a) 
date_start = '01-02-2013'    
date_stop = '07-28-2015'
start_1 = datetime.strptime(date_start, '%m-%d-%Y')
stop_1 = datetime.strptime(date_stop, '%m-%d-%Y')

days = abs((stop_1 - start_1).days)  

####b)  
date_start = '12312013'  
date_stop = '05282015'  
start_2 = datetime.strptime(date_start, '%m%d%Y')
stop_2 = datetime.strptime(date_stop, '%m%d%Y')

days = abs((stop_2 - start_2).days) 

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
start_3 = datetime.strptime(date_start, '%d-%b-%Y')
stop_3 = datetime.strptime(date_stop, '%d-%b-%Y')

days = abs((stop_3 - start_3).days) 