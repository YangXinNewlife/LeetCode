# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义是找出指定一的pivot number的index,就是pivot这个数字的左侧与右侧求和是一样的；
当存在这个pivot数字的时候，我们返回这边数字的索引即可，没有的话返回 - 1；
这里我们使用一个计和器 left_sum 来记录左侧的和，然后需要预先统计一下所有数据的nums_sum；
然后依次遍历每个元素，分别去判断左右的和是否一致即可 left_sum * 2 == nums_sum - nums[i]；
"""


class FindPivotIndex(object):

    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        nums_sum = sum(nums)
        left_sum = 0
        for i in range(length):
            if left_sum * 2 == nums_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1
