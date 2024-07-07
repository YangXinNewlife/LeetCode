# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
题意是给定一串字符串，包含给定的元素和该元素所在的下标位置。
那么最后判断每种元素都出现的下标有几个。
直接通过哈希表方式来进行存储判断。
"""


class RingsAndRods(object):

    def countPoints(self, rings: str) -> int:
        result = 0
        hash_r = set()
        hash_g = set()
        hash_b = set()
        for i in range(0, len(rings), 2):
            color = rings[i]
            index = int(rings[i + 1])
            if color == 'R':
                hash_r.add(index)
            elif color == 'G':
                hash_g.add(index)
            else:
                hash_b.add(index)

        for j in range(10):
            if j in hash_r and j in hash_g and j in hash_b:
                result += 1
        return result

