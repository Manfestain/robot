# _*_ coding:utf-8 _*_
'统计记录的聊天信息'

import re
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from collections import Counter

# 统计所有好友的消息数量
def amount():
    name = []
    rule = re.compile(r'\[.*.\]')   # 匹配以'['开头，以']'结尾的字符串

    with open('chatlog.txt', 'r') as f:   # 打开聊天记录
        for line in f:
            key = rule.search(line).group()   # 拿到匹配的结果，group()表示匹配的整个结果
            name.append(key[1:-1])
    counter = Counter(name)

    # 绘制柱状图
    # ind = np.linspace(1, 5)
    num = counter.keys().__len__()   # 获取记录中的好友个数
    X = [x for x in range(1, num + 1)]
    Y = list(counter.values())
    labels = list(counter.keys())
    print(labels)
    figure = plt.figure(1)  # 创建绘图区
    ax = figure.add_subplot(111)  # 在图1中创建子图1
    ax.bar(X, Y, 0.5, color="green")
    ax.set_xlabel(labels)
    # ax.set_xticks(ind)
    # ax.set_xticklabels(labels)
    ax.set_ylabel('COUNT')
    ax.set_title('Bar Chart')
    plt.grid(True)
    plt.show()


# 通过简单的字义分析聊天情感
def feeling():
    words = []
    num = 0
    bad_num = 0
    rule = re.compile(r'[哼气不难坏问题].*')
    rule2 = re.compile(r'\].*')
    with open('chatlog.txt', 'r') as f:
        for line in f:
            key = rule.search(line)
            key2 = rule2.search(line).group()
            num += key2[1:].__len__()   # 得到总的聊天字数
            if key != None:  # 可能有没匹配到的，返回为None
                words.append(key.group())
                bad_num += key.group().__len__()   # 总的不开心字数

    percent = 1.0 - (bad_num/num)
    print('聊天总字数: ', num)
    print('具有负面意义的字数: ', bad_num)
    print('结果: 本次谈话的愉快程度为 %.2f ' % percent)

