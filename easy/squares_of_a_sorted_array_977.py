# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义是给定的List元素平方后排序返回，
题目如果是O(n^2)或者O(nlogn)的情况直接sort排序函数即可。
但是这里要求是在O(n)内返回，那么就可以考虑归并排序方式。
那么就得考虑元素的正负问题，
如果都是正的，则从第一个开始遍历即可。
如果都是负的，则从第最后一个开始遍历即可。
如果有正有负的，则从需要两个指针，从中间（正负之间）向前后开始遍历即可。
"""


class SquaresOfASortedArray(object):

    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        result = list()
        j = 0
        while j < nums_len and nums[j] < 0:
            j += 1
        i = j - 1
        while 0 <= i and j < nums_len:
            if nums[i] ** 2 < nums[j] ** 2:
                result.append(nums[i] ** 2)
                i -= 1
            else:
                result.append(nums[j] ** 2)
                j += 1
        while i >= 0:
            result.append(nums[i] ** 2)
            i -= 1

        while j < nums_len:
            result.append(nums[j] ** 2)
            j += 1
        return result



