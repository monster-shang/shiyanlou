import socket,sys
try:
    host_index = sys.argv.index('--host')
    port_index = sys.argv.index('--port')
    host = sys.argv[host_index+1]
    port_temp = sys.argv[port_index+1]
    port = []
    if '-' in port_temp:
        port_temp = port_temp.split('-')
        for i in range(int(port_temp[0]),int(port_temp[1])+1):
            port.append(i)
    else:
        port.append(port_temp)
    for i in port:
        s = socket.socket()
        s.settimeout(0.1)
        if s.connect_ex((host,int(i))) == 0:
            print(str(i) + ' ' + 'open')
        else:
            print(str(i) + ' ' + 'close')
        s.close
except:
    print('Parameter Error')

