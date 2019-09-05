# -*-coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
数学公式
数组的元素之和 - 数组的长度 * 数组中最小元素
"""


class MinimumMovesToEqualArrayElements(object):

    def minMoves(self, nums):
        """
        :param nums:
        :return:
        """
        return sum(nums) - len(nums) * min(nums)



