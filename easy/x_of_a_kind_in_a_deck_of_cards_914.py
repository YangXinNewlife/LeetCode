# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是根据给的牌分组，每组最少两个，并且得相同。
我们可以考虑用最大公约数的方式，先统计每个数字出现的次数，然后用最大公约数判断是否可以除尽即可
都除尽就返回True, 没有除尽就返回False；
"""
import collections


class XOfAKindInADeckOfCards(object):

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        elem_counter = collections.Counter(deck)
        min_size = min(elem_counter.values())
        for i in range(2, min_size + 1):
            if all(j % i == 0 for j in elem_counter.values()):
                return True
        return False
