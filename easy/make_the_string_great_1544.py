# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是通过判断给定的字符串s中，是否存在两个相邻并且一个大写一个小写的字符，
存在的话就进行消除，否则就保留，最后按顺序输出所有保留的字符串。
逻辑就是利用数组list模拟栈的操作stack。
"""


class MakeTheStringGreat(object):

    def makeGood(self, s: str) -> str:
        result = list()
        for i in s:
            if len(result) > 0 and result[-1].upper() == i.upper() and result[-1] != i:
                result.pop(-1)
            else:
                result.append(i)
        return ''.join(result)
