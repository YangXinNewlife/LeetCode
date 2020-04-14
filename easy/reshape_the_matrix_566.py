# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'


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





