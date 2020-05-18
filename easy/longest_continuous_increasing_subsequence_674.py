# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意说的很清楚就是寻找最大连续递增子序列；
* 连续
* 递增
然后返回连续的个数，那么我们可以这么处理；
首先我们利用两个指针left_index、right_index；
然后每次挪动的时候需要去判断右边的边界right_index < len(nums) 
以及左指针的数据是否小于右指针的数据
然后记数count++
然后指针后移，更新我们返回的max（保留最大值即可）；
"""


class LongestContinuousIncreasingSubsequence(object):

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = 0
        left_index = 0
        if len(nums) == 0:
            return 0
        while left_index < len(nums):
            count = 1
            right_index = left_index + 1
            while right_index < len(nums) and nums[left_index] < nums[right_index]:
                count += 1
                left_index = right_index
                right_index += 1
            left_index = right_index
            result = max(result, count)
        return result





