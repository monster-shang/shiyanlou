#!/usr/bin/env python3
import csv
import sys
userfile = '/home/shiyanlou/shiyanlou/user.csv'
class UserData(object):
    def __init__(self):
        self.userdata=[]
        with open(userfile) as file:
            for x in file:
                gonghao,gongzi = x.split(',')
                gonghao = int(gonghao)
                gongzi = int(gongzi)
                yuanzu = (gonghao,gongzi)
                self.userdata.append(yuanzu)
        print(self.userdata)
a = UserData()
