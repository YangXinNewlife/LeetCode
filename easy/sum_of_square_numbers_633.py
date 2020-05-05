# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
此题目就是套用公式 a * a + b * b == c
a 与 b 进行增减1开始测试
"""
import math


class SumOfSquareNumbers(object):

    def judgeSquareSum(self, c: int) -> bool:
        temp_a = 0
        temp_b = int(math.sqrt(c))
        while temp_a <= temp_b:
            if temp_a * temp_a + temp_b * temp_b == c:
                return True
            if temp_a * temp_a + temp_b * temp_b < c:
                temp_a += 1
            else:
                temp_b -= 1
        return False
