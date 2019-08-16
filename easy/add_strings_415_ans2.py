# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
解题思路是利用zip_longest函数的特性，
返回两个list，并且会自动填充补位配置的参数。
"""
from itertools import zip_longest


class AddStrings(object):

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ""
        carry = 0
        for (x, y) in zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            s = (int(x) + int(y) + carry)
            d = s % 10
            carry = int(s / 10)
            res = str(d) + res
        if carry > 0:
            res = str(carry) + res
        return res
