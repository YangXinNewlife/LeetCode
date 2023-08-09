# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意其实就是遍历字符串s，每三个元素一组，看下组成的字符串是否都是不同的元素
直接用set去重判断即可。
"""


class SubstringsOfSizeThreeWithDistinctCharacters(object):

    def countGoodSubstrings(self, s: str) -> int:
        str_len = len(s)
        if str_len < 3:
            return 0
        result = 0
        for i in range(str_len - 3 + 1):
            if len(set(s[i:i + 3])) == 3:
                result += 1
        return result





