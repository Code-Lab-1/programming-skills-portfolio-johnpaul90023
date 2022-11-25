#Checks the current date and time in the present

import datetime
current = datetime.datetime.now()
print ("The current date and time is: ")
print (current.strftime("%Y-%m-%d %H:%M:%S"))