# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义是返回 A数组 加上 -K <= x <= K之后的B，B中最大值和最小值的最小差值。
那么我们可以考虑，把A的最大值 -K，A的最小值 +K，这样我们在算的事后即可求出最小的差值。
"""


class SmallestRangeI(object):

    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(max(A) - min(A) - 2 * K, 0)
