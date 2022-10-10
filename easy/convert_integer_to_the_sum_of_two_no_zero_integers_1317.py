# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
题意的要求就是给定一个数值n（非0）,
返回一组值[A, B], 
且A + B = n，
且 A 和 B 都不能包含 0，
因此直接遍历i，计算 i 和 n - i是否满足条件即可
"""


class ConvertIntegerToTheSumOfTwoNoZeroIntegers(object):

    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if not str(i).__contains__('0') and not str(n - i).__contains__('0'):
                return [i, n - i]
