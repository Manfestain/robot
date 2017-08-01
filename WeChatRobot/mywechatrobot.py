# _*_ coding:utf-8 _*_
'我的微信机器人'

import itchat
from tuling import getResponse
from saveText import saveMessage

# 获取当前聊天好友的信息
# @itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
# def getName(msg):
#     print(itchat.search_friends(userName=msg['FormUserName']))
#     return

# 微信个人机器人回复
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):

   name = itchat.search_friends(userName=msg['FromUserName'])['NickName']   # 获取昵称

   reply = getResponse(msg['Text']).get('text')   # 得到机器人回复

   saveMessage('[' + name + ']' + msg['Text'])   # 存储信息
   if name != itchat.search_friends()['NickName']:
       saveMessage('[' + '胡子先生' + ']' + reply)

   return reply

# 实现群聊机器人回复
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)   # isGroupchat判断是否是群聊
def text_reply(msg):
    # if (msg.isAT):   # isAT判断是否有人@自己
    #     itchat.send_msg("我已经收到了来自{0}的消息，实际内容是{1}".format(msg['ActualNickName'], msg['Text']), toUserName=msg['FromUserName'])
    return getResponse(msg['Text']).get('text')

itchat.auto_login()
itchat.run()