# -*- coding: UTF-8 -*-
from socket import socket
from json import loads
from base64 import b64decode

def main():
    client = socket()
    client.connect(('192.168.8.138', 5566))
    in_data = bytes()
    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata']
    with open(filename[:filename.find('.')]+'_1'+filename[filename.find('.'):], 'wb') as f:
        f.write(b64decode(filedata))
    print('jpg saved!')
if __name__=='__main__':
    main()