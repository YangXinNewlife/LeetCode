# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是给数字n的千位加"."，
说白了就是从后向前每三位加一个"."。
那我们就可以模拟这个操作，先将数字n转换为字符串后反转，
然后每三位加到返回的字符串中（开头补上"."）。

"""


class ThousandSeparator(object):

    def thousandSeparator(self, n: int) -> str:
        n_rev = str(n)[::-1]
        result = n_rev[:3]
        i = 3
        while i < len(n_rev):
            result += '.' + n_rev[i: i + 3]
            i += 3
        return result[::-1]
