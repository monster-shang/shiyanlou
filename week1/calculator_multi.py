#!/usr/bin/env python3
import csv
import sys
from multiprocessing import Process,Queue
queue1=Queue()
queue2=Queue()
args = sys.argv[1:] 
index = args.index('-o')
gongzifile = args[index+1]
class Config(object):  
    args = sys.argv[1:]      
    index = args.index('-c')
    configfile = args[index+1]
    def __init__(self):
        self.args = sys.argv[1:]      
        index = self.args.index('-c')
        self.configfile = self.args[index+1]
        self.config = {}
        with open(self.configfile) as file:
            for x in file:
                key,value = x.split('=')
                key = key.strip()
                value = float(value.strip())
                self.config[key] = value
    def JiShuL(self):
        return self.config['JiShuL']
    def JiShuH(self):
        return self.config['JiShuH']
    def YangLao(self):
        return self.config['YangLao']
    def YiLiao(self):
        return self.config['YiLiao']
    def ShiYe(self):
        return self.config['ShiYe']
    def GongShang(self):
        return self.config['GongShang']
    def ShengYu(self):
        return self.config['ShengYu']
    def GongJiJin(self):
        return self.config['GongJiJin']
Config = Config()
JiShuL=Config.JiShuL()
JiShuH=Config.JiShuH()
YangLao=Config.YangLao()
YiLiao=Config.YiLiao()
ShiYe=Config.ShiYe()
GongShang=Config.GongShang()
ShengYu=Config.ShengYu()
GongJiJin=Config.GongJiJin()
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
    args = sys.argv[1:]
    index = args.index('-d')
    userfile = args[index+1]
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
        z=(gonghao,gongzi,b,c,d)
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

