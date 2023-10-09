# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是判断字符串s是不是words元素拼接的前缀
"""


class CheckIfStringIsAPrefixOfArray(object):

    def isPrefixString(self, s: str, words: List[str]) -> bool:
        result = ""
        for i in words:
            result += i
            if s == result:
                return True
        return False


