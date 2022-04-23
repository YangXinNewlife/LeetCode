# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
解题思路其实就是判读啊给出的公交路径，和起点与终点。
判断正着走是比较短还是反着走比较短。
正着走 sum(distance[start:destination])
反着走 sum(distance) - sum(distance[start:destination])
"""


class DistanceBetweenBusStops(object):

    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        return min(sum(distance[start:destination]), sum(distance) - sum(distance[start:destination]))

