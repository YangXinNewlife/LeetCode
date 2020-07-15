# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给我们一个数字，例如10，我们需要判断从1 到 10的数组之间（包含10）中的 good number 有几个？
good number的含义是，180度反转数字后，如果数组不变成本身，并且有含义的化，那么就是 good number，
1 ～ 10: 
good number: 2 5 6 9 
not good number: 3 4 7
其中 1 0 8 是合法的但是不算 good number; 
"""


class RotatedDigits(object):

    def rotatedDigits(self, N: int) -> int:
        result = 0
        for i in range(1, N + 1):
            temp_i = str(i)
            if '3' in temp_i or '4' in temp_i or '7' in temp_i:
                continue
            if '2' in temp_i or '5' in temp_i or '6' in temp_i or '9' in temp_i and '0' in temp_i or '1' in temp_i or '8' in temp_i:
                result += 1
        return result















