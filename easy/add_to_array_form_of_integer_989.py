# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义就是数组加上数字在返回数组，
方法就是先数组转数字，然后相加后再转回数组。
"""


class AddToArrayFormOfInteger(object):

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = list()
        result_temp = int("".join(map(str, num))) + k
        if result_temp == 0:
            return [0]
        while result_temp:
            result.append(result_temp % 10)
            result_temp //= 10
        return result[::-1]


