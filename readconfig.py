class Config(object):
    def __init__(self):
        self.config = {}
        with open(filename) as file:
            for x in file:
                key,value = x.split('=')
                key = key.strip()
                value = value.strip()
                self.config[key] = value
        print(self.config)
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
x = Config()
print(x.JiShuH())
print(x.JiShuL())
print(x.YangLao())
print(x.YiLiao())
print(x.ShiYe())
print(x.GongShang())
print(x.ShengYu())
print(x.GongJiJin())
