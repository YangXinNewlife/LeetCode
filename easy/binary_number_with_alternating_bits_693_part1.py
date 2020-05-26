# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目想找到将给定的数字 n 转换为二进制时，0与1是否是间隔分布的，
因此我们只需要判断是否有00或者11出现即可；
"""


class BinaryNumberWithAlternatingBits(object):

    def hasAlternatingBits(self, n: int) -> bool:
        if "11" in bin(n) or "00" in bin(n):
            return False
        return True