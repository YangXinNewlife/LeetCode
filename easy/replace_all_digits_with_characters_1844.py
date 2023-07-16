# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意其实就是希望将给定字符串中基于奇数位的数字，
去变换偶数位的字符。
题目中最重要的两个函数
chr()函数数字专字符
ord()函数字符转数字
"""


class ReplaceAllDigitsWithCharacters(object):

    def replaceDigits(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            if i % 2 == 0:
                result += s[i]
            else:
                result += chr(ord(s[i-1]) + int(s[i]))
        return result

