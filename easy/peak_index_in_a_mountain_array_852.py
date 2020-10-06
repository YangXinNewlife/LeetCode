# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是找到有序数组中的峰值下标
并满足
arr.length >= 3
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
即可，那么我们直接找值最大的下标即可
"""


class PeakIndexInAMountainArray(object):

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))
