# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
题目直接打标处理，遍历每个元素排序后求和即可
"""
from collections import defaultdict
from string import digits


class MinimumSumOfFourDigitNumberAfterSplittingDigits(object):

    def minimumSum(self, num: int) -> int:
        num_list = list()
        num_list.append(int(str(num)[0]))
        num_list.append(int(str(num)[1]))
        num_list.append(int(str(num)[2]))
        num_list.append(int(str(num)[3]))
        num_list = sorted(num_list)
        return 10 * (num_list[0] + num_list[1]) + num_list[2] + num_list[3]


test = MinimumSumOfFourDigitNumberAfterSplittingDigits()
print(test.minimumSum(2932))



