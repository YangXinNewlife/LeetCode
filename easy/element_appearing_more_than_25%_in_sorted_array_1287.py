# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import collections
"""
Solutions:
题目的意思是想统计每个数组出现的次数，
当出现的数字个数占比大于等于0.25时,
返回该数字即可，默认返回第一个元素即可。
"""


class ElementAppearingMoreThanInSortedArray(object):

    def findSpecialInteger(self, arr: List[int]) -> int:
        arr_size = len(arr)
        arr_elem = collections.Counter(arr)
        for i in arr_elem:
            if (dict(arr_elem).get(i) / arr_size) > 0.25:
                return i
        return arr[0]
