# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个数组arr，然后找到这个数组中数值和出现次数一样的数中最大的那个，
如果没找到则返回-1，
"""
import collections


class FindLuckyIntegerInAnArray(object):

    def findLucky(self, arr: List[int]) -> int:
        result = -1
        arr_count = collections.Counter(arr)
        for i in arr_count.keys():
            if i == arr_count[i]:
                if i > result:
                    result = i
        return result
