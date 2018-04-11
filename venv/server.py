#!/usr/bin/env python
#-*- coding:utf-8 -*-
import socket
import sys

#创建 socket
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本地主机名
host = socket.gethostname()
port = 9999

#绑定端口号
serverSocket.bind((host,port))

#设置最大连接数。超过后排队
serverSocket.listen(5)
while True:
    #建立客户端连接
    clientsocket,addr = serverSocket.accept()

    print('链接地址:%s'% str(addr))

    msg = '欢迎访问菜鸟写的服务端'+"\r\n"
    dict = {'name':'huangzhi','sex':'man','age':'18'}
    clientsocket.send(str(dict).encode('utf-8'))
    clientsocket.close()