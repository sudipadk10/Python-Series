#To run this code type in terminal;
# python sysarg.py Name

import sys

if len(sys.argv) < 2:
   sys.exit("Too few arguments") #print and exit

for arg in sys.argv[1:]: # [1:] it will not print 0th index term called slice.
    
    print("My name is " , arg)