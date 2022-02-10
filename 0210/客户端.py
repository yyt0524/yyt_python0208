# -*- coding: UTF-8 -*-
from socket import socket

def main():
    #创建套接字对象使用ipv4
    client = socket()
    #链接到服务器
    client.connect(('192.168.8.138', 6789))
    #从服务器接受数据
    print(client.recv(1024).decode('utf-8'))
    client.close()

if __name__ == '__main__':
    main()