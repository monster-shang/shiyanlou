import re
from datetime import datetime
from collections import Counter
def open_parser(filename):
    with open(filename) as logfile:
        pattern = (r''
                   r'(\d+.\d+.\d+.\d+)\s-\s-\s'
                   r'\[(.+)\]\s'
                   r'"GET\s(.+)\s\w+/.+"\s'
                   r'(\d+)\s'
                   r'(\d+)\s'
                   r'"(.+)"\s'
                   r'"(.+)"')
        parsers = re.findall(pattern,logfile.read())
    return parsers
def main():
    logs = open_parser('/home/shiyanlou/Code/nginx.log')
    ip_list = []
    request404_list = []
    for log in logs:
        dt = datetime.strptime(log[1],'%d/%b/%Y:%H:%M:%S %z')
        if int(dt.strftime('%d')) == 11:
            ip_list.append(log[0])
        if int(log[3]) == 404:
            request404_list.append(log[2])
    ip = Counter(ip_list)
    ip = sorted(ip.items(),key=lambda x:x[1])
    request404 = Counter(request404_list)
    request404 = sorted(request404.items(),key=lambda x:x[1])
    ip_dict = dict([ip[-1]])
    url_dict = dict([request404[-1]])
    return ip_dict,url_dict
if __name__ == '__main__':
    ip_dict,url_dict = main()
    print(ip_dict,url_dict)

