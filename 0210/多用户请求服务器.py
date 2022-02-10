# -*- coding: UTF-8 -*-
from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread

def main():
    #自定义线程类
    class FileTransferHander(Thread):
        def __init__(self, client):
            super().__init__()
            self.client = client
        def run(self):
            my_dict = {}
            my_dict['filename'] = 'yyt.jpg'
            my_dict['filedata'] = data
            json_str = dumps(my_dict)
            self.client.send(json_str.encode('utf-8'))
            self.client.close()

    server = socket()
    server.bind(('192.168.8.138', 5566))
    server.listen(512)
    print('server is listening')
    with open('yyt.jpg', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        FileTransferHander(client).start()
if __name__=='__main__':
    main()
