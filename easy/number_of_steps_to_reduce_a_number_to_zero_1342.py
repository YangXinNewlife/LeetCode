# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一个数字num，
如果当前数是偶数，则除以2，否则减1，
这样累积经过多少步等于0。
直接按照这个逻辑算即可。
if num % 2 == 0:
    num /= 2
else:
    num -= 1
result += 1
"""


class NumberOfStepsToReduceANumberToZero(object):

    def numberOfSteps(self, num: int) -> int:
        result = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            result += 1
        return result

