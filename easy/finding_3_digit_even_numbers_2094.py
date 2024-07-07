# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
题目是给出一个数组，我们基于数组中元素进行三位数的偶数组合
第一位不能是0，那么返回所有可以组成的可能三位数。
"""


class Finding3DigitEvenNumbers(object):

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = list()
        digits_dict = {}
        for i in digits:
            digits_dict[i] = digits_dict.get(i, 0) + 1

        for j in range(100, 1000, 2):
            digits_1st = j // 100
            if digits_dict.get(digits_1st, 0) > 0:
                digits_dict[digits_1st] -= 1
            else:
                continue

            digits_2nd = j // 10 % 10
            if digits_dict.get(digits_2nd, 0) > 0:
                digits_dict[digits_2nd] -= 1
            else:
                digits_dict[digits_1st] += 1
                continue

            digits_3rd = j % 10
            if digits_dict.get(digits_3rd, 0) > 0:
                result.append(j)
            digits_dict[digits_1st] += 1
            digits_dict[digits_2nd] += 1
        return result
