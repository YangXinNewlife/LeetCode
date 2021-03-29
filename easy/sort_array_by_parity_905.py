# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是拆开给定数组的奇数和偶数，返回的时候要偶数在前，奇数在后并且有序的。
那么我们就可以利用python3中Sorted内置的参数key/Python2中可以指定cmp=。
key=lambda x: x % 2筛选出来偶数，优先级很高，奇数的优先级低即可。
"""


class SortArrayByParity(object):

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda x: x % 2)

