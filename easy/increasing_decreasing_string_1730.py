# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思就是给定字符串s，
然后按照如下逻辑输出所有的字符：
1.按照升序排列;
2.按照降序排列；
"""


class IncreasingDecreasingString(object):

    def sortString(self, s: str) -> str:
        result = ""
        s_sorted = sorted(set(s))
        while s:
            for i in s_sorted:
                if i in s:
                    result += i
                    s = s.replace(i, '', 1)
            for i in s_sorted[::-1]:
                if i in s:
                    result += i
                    s = s.replace(i, '', 1)
        return result






