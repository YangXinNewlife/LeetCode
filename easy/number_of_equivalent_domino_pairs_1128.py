# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
题目的含义是给出部分多米诺对数值，其中可以翻转。
我们要判断有几组相同数值（包括反转的）。
那么我们就先统计不能反转的情况下，利用0 ～ 9数据限制的优势。
通过 a * 10 + b（a较小）的方式计算。
最后再算下n个数的和，就是n对的组合 n * (n - 1) / 2 即可
"""


class NumberOfEquivalentDominoPairs(object):

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        elem_dict = dict()
        for i in dominoes:
            temp_elem = i[0] * 10 + i[1] if i[0] < i[1] else i[1] * 10 + i[0]
            if temp_elem in elem_dict:
                elem_dict[temp_elem] += 1
            else:
                elem_dict[temp_elem] = 1
        result = 0
        for j in elem_dict.values():
            result += int(j * (j - 1) / 2)
        return result

