# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意其实是给定两个数组，arr1 和 arr2
然后分别用arr1的每个元素去减arr2的每个元素的，求绝对值，如果绝对值都是大于2的，则符合距离值，
最后看下arr1中有几个符合，返回个数。

"""


class FindTheDistanceValueBetweenTwoArrays(object):

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0
        for i in arr1:
            count = 0
            for j in arr2:
                if abs(i - j) <= d:
                    break
                else:
                    count += 1
                if count == len(arr2):
                    result += 1
        return result

