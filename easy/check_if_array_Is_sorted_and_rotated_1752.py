# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个数组，要求判断经过变换处理后，
数组是否可以满足非递增（仅有可能出现一对重复元素）
那么直接遍历计算大小即可。
"""


class CheckIfArrayIsSortedAndRotated(object):

    def check(self, nums: List[int]) -> bool:
        result = 0
        nums_len = len(nums)
        for i in range(nums_len):
            if nums[i] > nums[(i + 1) % nums_len]:
                result += 1
        return False if result > 1 else True


