# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思就是给定一个数组，然后判断数组中每个元素出现的个数是否重复，
如果出现的次数不重复，那么返回true，否则返回false
"""
import collections


class UniqueNumberOfOccurrences(object):

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_counter = collections.Counter(arr)
        elem_cnt = arr_counter.values()
        return elem_cnt.__len__() == len(set(elem_cnt))
