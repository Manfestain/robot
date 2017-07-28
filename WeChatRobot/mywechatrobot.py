# _*_ coding:utf-8 _*_
'我的微信机器人'

import itchat
from tuling import getResponse

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return getResponse(msg['Text']).get('text')

itchat.auto_login()
itchat.run()