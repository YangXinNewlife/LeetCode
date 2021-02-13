# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'


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


