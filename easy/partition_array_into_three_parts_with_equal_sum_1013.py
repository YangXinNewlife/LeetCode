# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'

"""
Solutions:
题目的含义是判断数组是否可以三等分。
我们第一个想到就是使用两个指针，一起滑动判断指针内的和是否相等即可。
"""


class PartitionArrayIntoThreePartsWithEqualSum(object):

    def canThreePartsEqualSum(self, arr):
        arr_sum = sum(arr)
        if arr_sum % 3:
            return False
        left = 0
        right = len(arr) - 1
        left_sum, right_sum = arr[left], arr[right]
        while left + 1 < right:
            if left_sum == arr_sum / 3 and right_sum == arr_sum / 3:
                return True
            if left_sum != arr_sum / 3:
                left += 1
                left_sum += arr[left]
            if right_sum != arr_sum / 3:
                right -= 1
                right_sum += arr[right]
        return False
