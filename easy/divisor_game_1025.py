# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的含义是：
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。
只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

解题思路：
我们把问题简化，可以理解为是不是只要每个人玩的时候，
另一个人还可以玩一轮就赢了，那么我们只需要判断 N 能否被2整除即可，
可以整除说明两个人机会平均，爱丽丝就可以赢。
"""


class DivisorGame(object):

    def divisorGame(self, n: int) -> bool:
        if n % 2 == 0:
            return True
        else:
            return False
