# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是将各种十进制转换，包含了0和负数；
这里有一个简单的模板可以套用，十进制转N进制
result = ""
while num:
    r, num = num % a, num // a
    result = str(r) + result
这里是7进制，并且需要处理0和负数，我们先保留数据的原始符号。
然后再转换，最后把符号加上去。
"""


class Base7(object):

    def convertToBase7(self, num: int) -> str:
        res = '' if num != 0 else '0'
        flag = '-' if num < 0 else ''
        num = abs(num)
        while num:
            r, num = num % 7, num // 7
            res = str(r) + res
        return flag + res




