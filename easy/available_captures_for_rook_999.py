# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
分析：题目的要求就是计算车R能吃掉多少个卒P。
那么车可以上下左右四个方向运动，当遇到象B，则不能吃掉P。
因此我们先找到R，再统计各个方向可以直接接触到的P即可。
"""


class AvailableCapturesForRook(object):

    def numRookCaptures(self, board: List[List[str]]) -> int:
        x = y = result = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x = i
                    y = j
                    break
        for i in range(y, -1, -1):
            if board[x][i] == 'B':
                break
            if board[x][i] == 'p':
                result += 1
                break
        for j in range(y, 8):
            if board[x][j] == 'B':
                break
            if board[x][j] == 'p':
                result += 1
                break
        for i in range(x, -1, -1):
            if board[i][y] == 'B':
                break
            if board[i][y] == 'p':
                result += 1
                break
        for j in range(x, 8):
            if board[j][y] == 'B':
                break
            if board[j][y] == 'p':
                result += 1
                break
        return result


