# -*- coding:utf-8 -*-
__author__ = 'yangxin'
"""
Solutions:
题目很好理解，解题思路就是我们每三个处理一次，判断是否有0即可，有的话我们直接把n - 1，
最后判断小于等于0则返回True，如果不对的话就是False；
"""


class CanPlaceFlowers(object):

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
        return n <= 0

