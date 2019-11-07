# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import collections
"""
Solutions:
考虑这个问题我们可以利用
collections的Counter操作，将每个元素的个数做一个统计，然后分成三种情况，K - 两个元素的差值。
K < 0, 直接返回0；
K > 0, 返回 元素 + k等于元素的个数。
K = 0, 返回元素个数大于1的（即相减可以为0）即可。
"""


class KDiffPairsInAnArray(object):

    def findPairs(self, nums: List[int], k: int) -> int:
        c = collections.Counter(nums)
        if k < 0:
            return 0
        elif k > 0:
            return len(set(nums) & set(n + k for n in nums))
        elif k == 0:
            return sum(n > 1 for n in c.values())


