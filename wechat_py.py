#!/usr/bin/python3
# -*- coding: utf-8 -*-

import itchat
import time
from itchat.content import *

'''

'''
# 登录
# itchat.auto_login()

# 向个人文件助手发送消息
# itchat.send('Hello, filehelper', toUserName='filehelper')

'''
# 回复发给自己的文本消息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    today1 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    print(msg)
    return msg['Text']+':来自马克吐温服务器的回复。time:'+str(today1)
'''

# 回复文本
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

# # 以动态的方式发送图片/文件
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

# 回复文件
@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def download_files(msg):
    msg['Text'](msg['FileName'])
    itchat.send('@%s@%s'%('img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']), msg['FromUserName'])
    return '%s received'%msg['Type']

# 新增好友
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

itchat.auto_login()
# itchat.auto_login(enableCmdQR=True) # 使用命令行显示二维码
# itchat.auto_login(hotReload=True) # 退出程序后暂存登陆状态

itchat.run()
