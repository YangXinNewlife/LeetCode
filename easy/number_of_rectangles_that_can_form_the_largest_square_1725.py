# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意其实是找出来二维数组中，最小的数组中最大的个数。
直接遍历，求最大的，遇到更大的直接刷新result = 1
本题目也可以用哈希处理，最后求最大哈希的个数
"""


class NumberOfRectanglesThatCanFormTheLargestSquare(object):

    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        result = 0
        max_len = 0
        for l, w in rectangles:
            square = min(l, w)
            if square == max_len:
                result += 1
            elif square > max_len:
                max_len = square
                result = 1
        return result
