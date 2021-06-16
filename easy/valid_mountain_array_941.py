# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
解题分析，题目的意思是要找出来给出数组arr是否符合山的形状。
如题目中描述的结构，因此我们就只需要判断峰值在哪里即可。
因此我们是用双指针，分别从前后扫描，找到最大的那个，并且前后值的位置相同时，我们判断下是否在区间内即可。
"""


class ValidMountainArray(object):

    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i, j,  arr_length = 0, len(arr) - 1, len(arr)
        while (i + 1) < arr_length and arr[i + 1] > arr[i]:
            i += 1
        while (j - 1) >= 0 and arr[j - 1] > arr[j]:
            j -= 1
        return 0 < i == j < arr_length - 1

