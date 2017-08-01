# _*_ coding:utf-8 _*_
'测试程序'

import itchat
from itchat.content import *

# # 给文件传输助手发送一条消息
# itchat.auto_login()
# itchat.send('Hello, filehelper!', toUserName='filehelper')

# # 最简单的消息回复
# @itchat.msg_register(itchat.content.TEXT)
# def test_reply(msg):
#     # 返回同样的文本消息
#     return msg['FromUserName']
#
# itchat.auto_login()
# # 绑定消息响应事件，让itchat运行起来，监听消息
# itchat.run()

# 处理文本消息
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

# 处理多媒体消息
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def down_file(msg):
    msg['Text'](msg['Filename'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'Vid'}.get(msg['Type'], 'fil'), msg['Filename'])

# 处理好友添加请求
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

# 处理群消息
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I recived: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

# hotReload = True 可以保留登陆状态
itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.run()

# import urllib
# import json
# import requests
#
# message = '你好'.encode('utf-8')
# url = 'http://www.tuling123.com/openapi/api'
# data = {
#     "key": "21899823d93449ffa329eca31bba8f7e",
#     "info": message,
#     "userid": "9527"
# }
# r = requests.post(url, data=data)
# content = r.json().get('text')
# print(content)