# -*— coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是把给定数组，分批判断是否可以整除5，
由于每次由于会有前缀，相当于前缀左移，因此再和后面数值整合的时候，
就可以得出公式
pre * 2 + i
"""


class BinaryPrefixDivisibleBy5(object):

    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = list()
        pre = 0
        for i in nums:
            pre = (pre * 2 + i) % 5
            result.append(pre == 0)
        return result

