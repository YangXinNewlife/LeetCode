# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目就是判断给出的字符串sentence，是否包含26个小写字母即可。
使用数组集合。
"""
import collections


class CheckIfTheSentenceIsPangram(object):

    def checkIfPangram(self, sentence: str) -> bool:
        char_dict = collections.defaultdict(int)
        for i in sentence:
            char_dict[i] += 1
        result = len(char_dict)
        return result >= 26


