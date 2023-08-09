# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是基于a - 0, b - 1, c - 2的映射关系转换
将给定的firstWord和secondWord转换为数字，求和后判断是否和targetWord一致。
可以直接用Python自带的ord('0')函数即可。字符串转数字。
"""


class CheckIfWordEqualsSummationOfTwoWords(object):

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.str_to_dig(firstWord) + self.str_to_dig(secondWord) == self.str_to_dig(targetWord)

    def str_to_dig(self, str):
        return int("".join(chr(ord('0') + ord(i) - ord('a')) for i in str))

