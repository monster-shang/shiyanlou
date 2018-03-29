#!/usr/bin/env python3
import sys,getopt,csv,configparser
from multiprocessing import Process,Queue
from datetime import datetime
queue1=Queue()
queue2=Queue()
try:
    opts, args = getopt.getopt(sys.argv[1:], "ho:C:c:d:o:h:", ["help"])
except getopt.GetoptError:
    print("Error")
for o,a in opts:
    if o in ('-C'):
        city = a.upper()
    elif o in ('-c'):
        configfile = a
    elif o in ('-d'):
        userfile = a
    elif o in ('-o'):
        gongzifile = a
    elif o in ('-h'):
        print('Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata')
cf = configparser.ConfigParser()
cf.read(configfile)
JiShuL = cf.getfloat(city,'JiShuL')
JiShuH = cf.getfloat(city,'JiShuH')
YangLao = cf.getfloat(city,'YangLao')
YiLiao = cf.getfloat(city,'YiLiao')
ShiYe = cf.getfloat(city,'ShiYe')
GongShang = cf.getfloat(city,'GongShang')
ShengYu = cf.getfloat(city,'ShengYu')
GongJiJin = cf.getfloat(city,'GongJiJin')
class Money(object):
    def shebao(self,gongzi):
        JiShu = gongzi
        if JiShu < JiShuL:
            JiShu = JiShuL
        elif JiShu > JiShuH:
            JiShu = JiShuH
        shebao = JiShu*(YangLao+YiLiao+ShiYe+GongShang+ShengYu+GongJiJin)
        return shebao
    def jiaoshui(self,gongzi):
        a = gongzi - self.shebao(gongzi) - 3500
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
        return c
    def shuihou(self,gongzi):
        shuihou = gongzi - self.shebao(gongzi) - self.jiaoshui(gongzi)
        shuihou = format(shuihou,".2f")
        return shuihou
Money= Money()
def readuserdata():
    userdata = []
    with open(userfile) as file:
        for x in file:
            gonghao,gz = x.split(',')
            gonghao = int(gonghao)
            gz = int(gz)
            yuanzu = (gonghao,gz)
            userdata.append(yuanzu)
    queue1.put(userdata)
def jisuan():
    data=queue1.get()
    shuchu=[]
    for x in data:
        gonghao = x[0]
        gongzi = x[1]
        b = Money.shebao(gongzi)
        c = Money.jiaoshui(gongzi)
        d = Money.shuihou(gongzi)
        e = datetime.now().strftime('%Y-%m-%d %H:%m:%S')
        z=(gonghao,gongzi,b,c,d,e)
        shuchu.append(z)
    newdata=shuchu
    queue2.put(newdata)
def out():
    o = queue2.get()
    for x in o:
        with open(gongzifile,'a')as file:
            file.write(str(x))
readuserdata()
jisuan()
out()
