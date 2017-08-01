# _*_ coding:utf-8 _*_
'存储聊天记录'

import time

def getTime():
    return time.strftime("%Y-%m-%d %H:%M:%S  ", time.localtime())   # 格式化时间,此处表示月和日的字符必须小写

def saveMessage(info):
    message = getTime() + info + '\n'  # 给消息加上确定的时间
    with open('chatlog.txt', 'a') as f:
        f.write(message)
