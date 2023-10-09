# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是判断给定的字符串s中的每个元素是不是出现的次数都一样
直接Counter(s)统计每个元素出现的个数，然后在遍历比较即可
"""
import collections


class CheckIfAllCharactersHaveEqualNumberOfOccurrences(object):

    def areOccurrencesEqual(self, s: str) -> bool:
        s_collect = list(collections.Counter(s).values())
        return all(i == s_collect[0] for i in s_collect)
