# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
from collections import Counter
"""
Solutions:
题目含义是给出两组数组
arr1 较长的数组
arr2 参照数组
我们要把arr1重新排序，其中把arr1中出现arr2的数组按照arr2的顺序排在前面，
其余的在排序在后面。
我们直接遍历arr2,将数组加到返回的结果，然后再把剩下的加进去即可。

"""


class RelativeSortArray(object):

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = list()
        temp_list = list()
        arr1_cnt = Counter(arr1)
        for i in arr2:
            result .extend(arr1_cnt[i] * [i])
            del arr1_cnt[i]
        for j in arr1_cnt:
            temp_list.extend(temp_list[j] * [j])
        result.extend(sorted(temp_list))
        return result


