# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import heapq
"""
Solutions:
该题目的含义是给出一个数字组成列表，给出一个K，代表要翻转几次，每次翻转由 i -> -i, 其中也可以一直翻转相同的元素。
如果我们维护一个最小堆，每次翻转都是翻转最小的，那么翻转后的和就可以保证是操作后最大的。
"""


class MaximizeSumOfArrayAfterKNegations(object):

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums_sum = sum(nums)
        heapq.heapify(nums)
        while k > 0:
            curr_min = heapq.heappop(nums)
            heapq.heappush(nums, -curr_min)
            k -= 1
            nums_sum += -curr_min * 2
        return nums_sum
