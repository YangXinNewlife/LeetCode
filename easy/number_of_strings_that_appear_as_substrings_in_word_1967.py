# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
还是两个字符串如何判断是否子串，这里直接遍历匹配计数就可以。
"""


class NumberOfStringsThatAppearAsSubstringsInWord(object):

    def numOfStrings(self, patterns: List[str], word: str) -> int:
        result = 0
        for i in patterns:
            if word.__contains__(i):
                result += 1
        return result
