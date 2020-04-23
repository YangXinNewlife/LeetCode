# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意：每次对于 0 <= i < a and 0 <= j < b范围内的数进行+1操作，求最终最大的数的个数；
解决方法：
最大的数字每次都会集中在矩阵的左上角；
最大的数字是每次都会 + 1的位置，这些位置就是 0<= i <= min_a 和 0 <= i < min_b，所以个数就是min_a * min_b；
"""


class RangeAdditionII(object):

    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min(i[0] for i in ops) * min(i[1] for i in ops) if ops else m * n