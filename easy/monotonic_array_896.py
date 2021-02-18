# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是找出来给出的数组是否是单调数组（单调递增或者单调递减），直接遍历数组判断相邻的属否有递增或者递减即可，
all函数的含义就是A中是否都是递增或者递减趋势
"""


class MonotonicArray(object):

    def isMonotonic(self, A: List[int]) -> bool:
        return all(A[i] - A[i + 1] >= 0 for i in range(len(A) - 1)) or \
               all(A[j] - A[j + 1] <= 0 for j in range(len(A) - 1))
