# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是判断给定的数组是否可以有满足Special的元素
1.X是要求数组中的数据有 arr[i] >= X
2.X == size(arr[i] >= X)
因为题目限制了大小
0 <= nums[i] <= 1000
因此直接暴力求解即可
"""


class SpecialArrayWithXElementsGreaterThanOrEqualX(object):

    def specialArray(self, nums: List[int]) -> int:
        for i in range(1, 1001):
            cnt = 0
            for j in nums:
                if j >= i:
                    cnt += 1
            if cnt == i:
                return cnt
        return -1
