#-*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是：
给定一个由不同数字组成的mxn矩阵，以任意顺序返回矩阵中的所有幸运数字。
幸运数是矩阵中的一个元素，它是行中的最小元素，列中的最大元素。
因此我们需要先找出来每行最小的数集合，因为题目保证不重复，因此我们使用set存储：
min_elems = {min(i) for i in matrix}
再矩阵转置后
zip(*matrix)
取每行最大的集合
最后求交集即可
"""


class LuckyNumbersInAMatrix(object):

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_elems = {min(i) for i in matrix}
        max_elems = {max(j) for j in zip(*matrix)}
        return list(min_elems & max_elems)

