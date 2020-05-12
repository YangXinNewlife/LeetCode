# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意：题目不难，但是一定要看懂题目的含义，这里的说的是为每个矩阵计算矩阵包含的八个以及自己（最多共九个）的元素平均值，
给出的实例解释如下：
当我们算第一个M[0]的时候，它的单元格是(0, 0)
所需要计算的是(0,2), (2,0), (2,2)所围绕的三个，以及(0,0)自己，
因此计算出来的结果就是floor(3/4) = floor(0.75) = 0，然后我们最后只保留整数，因此我们要用int处理结果；

"""
from copy import deepcopy


class ImageSmoother(object):

    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        if not M or not M[0]:
            return M
        rows = len(M)
        cols = len(M[0])
        is_valid = lambda i, j: i >= 0 and i < rows and j >= 0 and j < cols
        result = deepcopy(M)
        for row in range(rows):
            for col in range(cols):
                sum_num, count = 0, 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if is_valid(row + i, col + j):
                            sum_num += M[row + i][col + j]
                            count += 1
                result[row][col] = int(sum_num / count)
        return result

