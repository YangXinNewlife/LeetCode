# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给订两个字符串，然后判断下两个字符串的元素出现次数，如果有超过3个的则返回False,
所有都没超过则返回True
"""


class CheckWhetherTwoStringsAreAlmostEquivalent(object):

    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        words_dict = dict()
        for i in word1:
            words_dict[i] = words_dict.get(i, 0) + 1
        for j in word2:
            words_dict[j] = words_dict.get(j, 0) - 1

        for k in words_dict.values():
            if abs(k) > 3:
                return False
        return True

