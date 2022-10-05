# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是给出一个字符串s，其中将数字映射为字符。
正常就是单字符映射为一个字符。
#前两个映射为一个字符，因此需要用正则表达式来做一下切分。
'\d\d#|\d' -> 将字符串换位多组。
1326# -> 1、3、26 -> a、c、z
"""
import re


class DecryptStringFromAlphabetToIntegerMapping(object):

    def freqAlphabets(self, s: str) -> str:
        return re.sub(r'\d\d#|\d', lambda x: chr(int(x.group()[:2]) + 96), s)

