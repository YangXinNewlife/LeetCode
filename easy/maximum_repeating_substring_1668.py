# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意其实是判断给出的word最大重复多少次还是sequence的子串
所以直接打表处理即可
"""


class MaximumRepeatingSubstring(object):

    def maxRepeating(self, sequence: str, word: str) -> int:
        result = 0
        temp_word = word
        while sequence.__contains__(temp_word):
            result += 1
            temp_word += word
        return result

