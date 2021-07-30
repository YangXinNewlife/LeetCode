# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是找到周长最大的三角形，并返回周长。
三角形定义：
两边之和大于第三边。
我们只需要将数组排序，并且按照连续三个求和，判断是否满足要求即可。
满足要求返回三边的和即可。
"""


class LargestPerimeterTriangle(object):

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums_len = len(nums)
        for i in range(nums_len - 1, 1, -1):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                return nums[i - 2] + nums[i - 1] + nums[i]
        return 0

