# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意其实是从字符串中，找到所有的数字
并且去掉前导0的数字，判断下有多少个即可，
通过set和正则re.findall("\d+", word)操作即可
"""
import re


class NumberOfDifferentIntegersInAString(object):

    def numDifferentIntegers(self, word: str) -> int:
        word = re.findall("\d+", word)
        word_new = list()
        for i in word:
            word_new.append(str(i).lstrip("0"))
        return len(set(word_new))

