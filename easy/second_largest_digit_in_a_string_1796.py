# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import re
"""
Solutions:
题意是找出来给定的字符串中，数字第二大的，
没有第二大的或者没有数字，返回-1
核心处理，正则表达式，冲字符串中，抽取出来数字
re.findall('[0-9]{1}', s)
"""


class SecondLargestDigitInAString(object):

    def secondHighest(self, s: str) -> int:
        if s.isalpha():
            return -1
        s = set([int(i) for i in re.findall('[0-9]{1}', s)])
        if len(s) == 1:
            return -1
        else:
            s = list(s)
            s.sort()
            return s[-2]


