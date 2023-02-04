# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义是给定一个纯数字的数组nums，
先按照数字的频率排序，然后输出（升序），
如果遇到频率相同的，则逆序输出。
这里我们可以使用
lambda来定制规则，正常则使用频率升序，如果相同则反向，就是逆序即可。
"""
import collections


class SortArrayByIncreasingFrequency(object):

    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_Count = collections.Counter(nums)
        nums.sort(key=lambda i: (nums_Count[i], -i))
        return nums
