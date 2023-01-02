# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义是给定n个数字，然后几组跑步方向的顺序。
可以直接判断起点和终点，有两种情况：
1.如果终点大于起点,则可以直接返回起点到终点的所有覆盖点。
2.如果起点大于终点，则反向判断即可。
"""


class MostVisitedSectorInACircularTrack(object):

    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start = rounds[0]
        end = rounds[-1]
        if start <= end:
            return list(range(start, end + 1))

        else:
            exclude = list(range(end + 1, start))
            return [i for i in range(1, n + 1) if i not in exclude]
