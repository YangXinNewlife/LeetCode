# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
解题的方法我们可以来推演一下：
1.1个石子，先手赢；
2.2个石子，先手赢；
3.3个石子，先手赢；
4.4个石子，先手怎么拿，后手都赢；
5.5个石子，先手拿一个，后手怎么拿都输；
6.6个石子，先手拿一个，后手怎么拿都输；
7.7个石子，先手拿一个，后手怎么拿都输；
8.8个石子，后手怎么拿都赢；
以此类推，当我们发现每当出现石子的个数是4以及4的倍数的时候，
后手都会赢。
因此我们得到公式：
False if n % 4 == 0 else True
"""


class NimGame(object):

    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n % 4 == 0 else True

