#!/usr/bin/env python3
import sys
try:
    gongzi = int(sys.argv[1])
except:
    print('Parameter Error')
a = gongzi-3500
if a <= 0:
    c = 0
elif a <= 1500:
    c = a*0.03
elif 1500<a<=4500:
    c = a*0.1-105
elif 4500<a<=9000:
    c = a*0.2-555
elif 9000<a<=35000:
    c = a*0.25-1005
elif 35000<a<=55000:
    c = a*0.3-2755
elif 55000<a<=80000:
    c = a*0.35-5505
elif 80000<a:
    c = a*0.45-13505
c = format(c,".2f")
print(c)

