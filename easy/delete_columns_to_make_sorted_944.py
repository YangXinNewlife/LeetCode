# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
解题思路是要删除最少的列保证剩下所有的列都是有序的即可（递增）。
每次操作一步排序，判断是否有序即可。
"""


class DeleteColumnsToMakeSorted(object):

    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        len_str = len(strs[0])
        for i in range(len_str):
            column = [elem[i] for elem in strs]
            if column != sorted(column):
                result += 1
        return result
