# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的名字就是二分搜索，
再去看一下题意描述，没有问题，直接写吧
当target == nums[mid] return mid;
当target > nums[mid],说明在mid右侧，则mid + 1;
当target < nums[mid],说明在mid左侧，则mid - 1;
"""


class BinarySearch(object):

    def search(self, nums, target):
        left_index, right_index = 0, len(nums) - 1
        while left_index <= right_index:
            mid = (left_index + right_index) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                left_index = mid + 1
                self.search(nums[left_index: right_index], target)
            else:
                right_index = mid - 1
        return -1
