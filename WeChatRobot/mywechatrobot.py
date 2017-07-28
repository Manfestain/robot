# _*_ coding:utf-8 _*_
'我的微信机器人'

import itchat
from tuling import getResponse

@itchat.msg_register(itchat.content.TEXT)   # 监听
def text_reply(msg):
    return getResponse(msg['Text']).get('text')   # 返回为json,利用get()方法拿到机器人的回复

itchat.auto_login()  # 登陆
itchat.run()