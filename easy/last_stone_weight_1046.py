# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义是找出来给定数组中最大的两个，然后相减。
将非空的结果放到剩余的数组中，我们的思路有两个：
1.大鼎堆
2.数组比较操作
我们这里判断数组中剩余的元素，最后一个的时候返回。
"""


class LastStoneWeight(object):

    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.append(stones.pop(stones.index(max(stones))) - stones.pop(stones.index(max(stones))))
        return stones[0]
