#!/usr/bin/env python
#-*- coding:utf-8 -*-
#导入 socket sys 模块
import  socket
import sys

#创建socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本地主机名

host = socket.gethostname()

#设置端口、
port = 9999

#连接服务器，指定主机和端口
s.connect((host,port))

#接收小于 1024 字节的数据
msg = s.recv(1024)

s.close()
print(msg.decode('utf-8'))
