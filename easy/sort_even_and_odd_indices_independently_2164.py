# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
题意其实是对奇数和偶数分别进行排序，那么采用分治的思想，分别取出再排序即可。
最后基于奇数数和偶数特点进行返回即可
"""

class SortEvenAndOddIndicesIndependently(object):

    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd_list = sorted(nums[1::2], reverse=True)
        even_list = sorted(nums[::2])
        for j in range(0, len(even_list)):
            nums[j * 2] = even_list[j]
        for j in range(0, len(odd_list)):
            nums[j * 2 + 1] = odd_list[j]
        return nums
