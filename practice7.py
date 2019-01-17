# -*- coding:utf-8 -*-


def rect(height=5,width=5,symbol='*'):
    for i in range(height):
        # print(symbol * width)
        # 通过 字符串 * 数字 的方法可以重复输出字符
        for j in range(width):
            print(symbol,end='')
        print("\n",end='')


rect()
rect(4,3)
rect(2,6,symbol='!')
