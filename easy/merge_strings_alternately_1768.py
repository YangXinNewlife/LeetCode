# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定两个字符串，然后依次进行拼接
处理逻辑就先先找出来公共的长度，然后将非公共的部分补充在里面即可。
"""


class MergeStringsAlternately(object):

    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        min_len = min(len(word1), len(word2))
        temp_index = 0
        for i in range(min_len):
            result += word1[i] + word2[i]
            temp_index = i
        result += word1[temp_index + 1:]
        result += word2[temp_index + 1:]
        return result

