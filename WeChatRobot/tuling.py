# _*_ coding:utf-8 _*_

import requests

# 发送请求
def getResponse(_info):
    message = _info.encode('utf-8')  # 查看官方文档得知，必须以utf-8进行编码
    apiUrl = 'http://www.tuling123.com/openapi/api'  # 机器人请求的url
    data = {
        'key': '21899823d93449ffa329eca31bba8f7e',   # 机器人的APIKEY
        'info': message,
        'useid': 'wochat-robot'
    }
    r = requests.post(apiUrl, data=data).json()  # 使用requests请求
    return r