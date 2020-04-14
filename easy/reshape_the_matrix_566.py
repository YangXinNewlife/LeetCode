# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是将原有的len(nums)行、len(nums[0])列的矩阵，reshape为r行，c列；
如果转换不了直接返回原有矩阵
"""


class ReshapeTheMatrix(object):

    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c:
            return nums

        result = []
        row = []
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                row.append(nums[i][j])
                if len(row) == c:
                    result.append(row)
                    row = []
        return result





