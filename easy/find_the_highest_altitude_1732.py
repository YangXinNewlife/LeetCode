# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意的核心就是从0开始累加每个元素的和，然后找出来当前最大的之，
整个数组计算后，返回最大的值即可。
"""


class FindTheHighestAltitude(object):

    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        temp = 0
        for i in gain:
            temp += i
            result = max(temp, result)
        return result







