# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是给出一组正数的序列，然后给出一个k值
返回正数原有序列中缺失的部分的第k个数。
通过去重的原理，使用set去做处理，计算一个完整的序列all_set，
然后再计算一个现有的arr_set。
最后求减法即可。
"""


class KthMissingPositiveNumber(object):

    def findKthPositive(self, arr: List[int], k: int) -> int:
        all_set = set([i for i in range(1, arr[-1] + k + 1)])
        arr_set = set(arr)
        diff = list(all_set - arr_set)
        return sorted(diff)[k - 1]


