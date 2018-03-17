#!/usr/bin/env python3
import sys
import csv
args = sys.argv[1:]
c = args.index('-c')
d = args.index('-d')
o = args.index('-o')
configfile = args[c+1]
userdatefile = args[d+1]
incometax = args[o+1] 
class Config(object):
    def __init__(self):
        self.config = self._read_config()
    def _read_config(self):
        filename=configfile
        config = {}
        try:
            with open(filename) as file:
                for x in file:
                   key,value = x.split('=')
                   key = key.strip()
                   value = value.strip()
                   config[key] = value
        except:
            print('a')
Config()
l = config[JiShul]*config[ShenYu]
print(l)
