# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
解题思路：
一个数组有2N个数字，其中有N + 1个不同的数字。
在这里边恰好有一个数字重复了 N 次，我们需要找出这个重复了 N 次的数字是什么，
由 2N 到 N，刚好我们可以判断某一类数字的个数是 LEN(nums) / 2即可，我们利用
collections.Counter(nums)统计各个数字的个数，判断一下即可。
"""
import collections


class NRepeatedElementInSize2NArray(object):

    def repeatedNTimes(self, nums: List[int]) -> int:
        result_len = len(nums) / 2
        counter = collections.Counter(nums)
        for elem, cnt in counter.items():
            if cnt == result_len:
                return elem
        return 0

