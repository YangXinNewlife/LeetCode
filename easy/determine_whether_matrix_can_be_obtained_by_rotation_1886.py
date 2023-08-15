# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是经过三次变换后，target是否和mat一致，
因为第四期其实就是他自己肯定想等。
因此只需要判断当前元素与移动后的元素不同即可。
"""


class DetermineWhetherMatrixCanBeObtainedByRotation(object):

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        mat_len = len(mat)
        result = set()
        for i in range(mat_len):
            for j in range(mat_len):
                if mat[i][j] != target[i][j]:
                    result.add(0)
                if mat[i][j] != target[j][mat_len - i - 1]:
                    result.add(1)
                if mat[i][j] != target[mat_len - i - 1][mat_len - j - 1]:
                    result.add(2)
                if mat[i][j] != target[mat_len - j - 1][i]:
                    result.add(4)
                if len(result) == 4:
                    return False
        return True



























