# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions：
题目的含义是计算每个点到给定带你的距离，然后
按照距离远近升序方式排序返回。
我们这里使用：
result.append((abs(rCenter - i) + abs(cCenter - j), [i, j]))
存储距离和对应元素，
最后返回元素即可
"""


class MatrixCellsInDistanceOrder(object):

    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        result = list()
        for i in range(rows):
            for j in range(cols):
                result.append((abs(rCenter - i) + abs(cCenter - j), [i, j]))
        result.sort()
        return [k for d, k in result]
