#!/usr/bin/env python3
import csv
import sys
try:
    class Arge(object):
        def __init__(self):
            self.args = sys.argv[1:]
        def config(self):        
            index = self.args.index('-c')
            configfile = self.args[index+1]
            return configfile
        def user(self):
            index = self.args.index('-d')
            userfile = self.args[index+1]
            return userfile
        def output(self):
            index = self.args.index('-o')
            gongzifile = self.args[index+1]
            return gongzifile
except:
    print('Parameter Error')
arg = Arge()
configfile=arg.config()
userfile = arg.user()
gongzifile = arg.output()
class Config(object):
    def __init__(self):
        self.config = {}
        with open(configfile) as file:
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
class UserData(object):
    def __init__(self):
        self.userdata=[]
        with open(userfile) as file:
            for x in file:
                gonghao,gz = x.split(',')
                gonghao = int(gonghao)
                gz = int(gz)
                yuanzu = (gonghao,gz)
                self.userdata.append(yuanzu)
    def jisuan(self):
        shuchu=[]
        for x in self.userdata:
            gonghao = x[0]
            gongzi = x[1]
            b = Money.shebao(gongzi)
            c = Money.jiaoshui(gongzi)
            d = Money.shuihou(gongzi)
            with open(gongzifile,'a') as file:
                file.write(str(gonghao)+','+str(gongzi)+','+str(b)+','+str(c)+','+str(d)+'\n')
UserData = UserData()
UserData.jisuan()



