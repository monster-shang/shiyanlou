#!/usr/bin/env python3
import sys
import getopt
try:
    opts, args = getopt.getopt(sys.argv[1:], "ho:C:c:d:o:h:", ["help"])
except getopt.GetoptError:
    print("Error")
for o,a in opts:
    if o in ('-C'):
        city = a.upper()
    elif o in ('-c'):
        configfile = a
    elif o in ('d'):
        userfile = a
    elif o in ('o'):
        gongzifile = a
    elif o in ('-h'):
        print('Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata')
    print(o,a)
print(opts)
print(city)
