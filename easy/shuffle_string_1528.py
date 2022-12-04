# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给字符串重新排序，
排序的顺序就是给定的indices，
直接数组转字符串即可
"""


class ShuffleString(object):

    def restoreString(self, s: str, indices: List[int]) -> str:
        length = len(indices)
        result = [-1] * length
        for i in range(length):
            result[indices[i]] = s[i]
        return "".join(result)





