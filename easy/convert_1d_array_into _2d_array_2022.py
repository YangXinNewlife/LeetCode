# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
模拟操作，给定一个一位数组，利用规律使其变为二维数组。
这里就通过盘点给定一位数组的长度是否等于m*n直接判断是否可变换。
然后通过两个for遍历赋值即可
"""


class Convert1DArrayInto2DArray(object):

    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = list()
        if len(original) != m * n:
            return result
        result = [[0] * n for i in range(m)]
        for j in range(m):
            for k in range(n):
                result[j][k] = original[j * n + k]
        return result



