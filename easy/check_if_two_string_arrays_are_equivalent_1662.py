# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定2组字符串，判断两组字符串是否相同，直接循环遍历判断是否相同即可。
"""


class CheckIfTwoStringArraysAreEquivalent(object):

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        temp_result1 = ""
        temp_result2 = ""
        for i in range(len(word1)):
            temp_result1 += word1[i]
        for j in range(len(word2)):
            temp_result2 += word2[j]
        if temp_result1 == temp_result2:
            return True
        else:
            return False
