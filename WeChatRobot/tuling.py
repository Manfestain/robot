# _*_ coding:utf-8 _*_

import requests

def getResponse(_info):
    message = _info.encode('utf-8')
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '21899823d93449ffa329eca31bba8f7e',
        'info': message,
        'useid': 'wochat-robot'
    }
    r = requests.post(apiUrl, data=data).json()
    return r