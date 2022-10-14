# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个矩阵，然后一个k值
返回K个最快走完的行，其实就是统计每行的1的个数，然后排序，
返回前K个的下标，为了方便记录和排序，我们把1的个数和所在行用字段dict存储，
然后循环每次返回最小的即可。
"""


class TheKWeakestRowsInAMatrix(object):

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        result = list()
        temp_dict = {}
        for i in range(len(mat)):
            temp_cnt = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    temp_cnt += 1
                else:
                    break
            temp_dict[i] = temp_cnt
        for l in range(k):
            key_min = min(temp_dict.keys(), key=(lambda ii: temp_dict[ii]))
            result.append(key_min)
            temp_dict.pop(key_min)
        return result



