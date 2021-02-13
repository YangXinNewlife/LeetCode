# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意：
给出两个数组A、B
我们需要交换A、B中的数字，达到A、B两个数组分别求和相等；
思路：
我们可以分别算下 (SUM(A) + SUM(B)) / 2 是多少，
这样我们去算下，A中去掉什么，并且加上B中的数字刚好凑到就是答案； 
"""

class FairCandySwap(object):

    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_a = sum(A)
        sum_b = sum(B)
        set_b = set(B)
        middle = (sum_a + sum_b) // 2
        for i in A:
            temp_b = middle - (sum_a - i)
            if temp_b in set_b:
                return [i, temp_b]
        return []


