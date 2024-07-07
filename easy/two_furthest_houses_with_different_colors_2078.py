# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意其实就是找出来所给的数组中，两个值不相同的最远距离
这里使用贪心算法，一个从最左边开始和最右边的比，一个从最右边开始和最左边的比。
找到即返回。
"""


class TwoFurthestHousesWithDifferentColors(object):

    def maxDistance(self, colors: List[int]) -> int:
        result = 0
        list_len = len(colors)
        for i in range(list_len):
            if colors[i] != colors[list_len - 1]:
                result = max(result, list_len - 1 - i)
                break
        for j in range(list_len - 1, -1, -1):
            if colors[j] != colors[0]:
                result = max(result, j)
                break
        return result
