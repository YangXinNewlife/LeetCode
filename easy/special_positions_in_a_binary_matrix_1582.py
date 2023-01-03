# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定了特殊位置（当前数据值为1，且该行和列其余数为0）
则有特殊位置的该行或者该列求和应该是1，
因此我们先记录下特殊的行和列，然后分别计算求和即可。
zip(*mat)中的*mat为矩阵转置
"""


class SpecialPositionsInABinaryMatrix(object):

    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [i for i, row in enumerate(mat) if sum(row) == 1]
        cols = [j for j, col in enumerate(zip(*mat)) if sum(col) == 1]
        return sum([mat[k][l] for k in rows for l in cols])
