# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
计算最小公约数的逻辑，直接找到最小的长度，然后遍历比较即可，打表过。
"""
import collections


class CountCommonWordsWithOneOccurrence(object):

    def countWords(self, words1: List[str], words2: List[str]) -> int:
        result = 0
        words1_dict = collections.Counter(words1)
        words2_dict = collections.Counter(words2)
        if words1_dict.__sizeof__() >= words2_dict.__sizeof__():
            min_dict = words2_dict
        else:
            min_dict = words1_dict
        for i in min_dict:
            if words1_dict.get(i) == words2_dict.get(i) == 1:
                result += 1
        return result

