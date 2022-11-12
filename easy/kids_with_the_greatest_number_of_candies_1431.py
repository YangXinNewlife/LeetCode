# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思其实就是给定一个数组candies，
然后再额外给出一个数extraCandies，
然后判断把这额外的数给到哪一个元素上就是大于等于已有元素中最大的。
是的话该位置返沪True，否则返回False即可
"""


class KidsWithTheGreatestNumberOfCandies(object):
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = list()
        max_cnt = max(candies)
        for i in range(len(candies)):
            if extraCandies + candies[i] >= max_cnt:
                result.append(True)
            else:
                result.append(False)
        return result




