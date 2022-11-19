# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定两个数组，arr和目标数组target，然后判断是否可以通过修改arr中的子集，
然后反转，如果可以和target相同，则返回true，
解决方法是可以判断元素是否相同即可。
"""
import collections


class MakeTwoArraysEqualByReversingSubarrays(object):

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return collections.Counter(target) == collections.Counter(arr)
