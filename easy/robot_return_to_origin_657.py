# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
根据题意可以理解为不用考虑Robot的面向，所以我们只需要考虑方向即可，
两种方法：
1.将方向转化为数字 1 或 -1 我们最后判断是否等于 0 就可以了；
2.我们直接去统计 U和D 或者 L和R 的出现次数是否相等（即抵消）；
这里我们使用第二种方式解题；
"""
import collections


class RobotReturnToOrigin(object):

    def judgeCircle(self, moves: str) -> bool:
        hash_count = collections.Counter(moves)
        return hash_count['U'] == hash_count['D'] and hash_count['L'] == hash_count['R']



