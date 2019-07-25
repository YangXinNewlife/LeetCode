# -*- coding:utf-8 -*-
__author__ = 'yangxin'
import collections
"""
Soultions:
贪心算法并且维护两个队列
队列中我们存放 R 与 D 元素所在的下标。
存放好后，我们两个队列同时左边出队列，并且比较，
队R 中所出队的元素下标如果小于 队D 中所出队的元素下标，
则我们把胜利的一方元素R，放回队尾（当前元素的下标 + n）
失败的则直接出队。
就这样最后剩下的就是胜利者。
"""


class BinaryTreePaths(object):

    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        queue_r, queue_d = collections.deque(), collections.deque()
        n = len(senate)
        for i, s in enumerate(senate):
            if s == 'R':
                queue_r.append(i)
            else:
                queue_d.append(i)
        while queue_r and queue_d:
            r = queue_r.popleft()
            d = queue_d.popleft()
            if r < d:
                queue_r.append(r + n)
            else:
                queue_d.append(d + n)
        return "Radiant" if queue_r else "Dire"
