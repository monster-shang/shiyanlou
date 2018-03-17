filename = '/home/shiyanlou/shiyanlou/test.cfg'
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
