# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思就是看三字棋谁赢？
规则跟五子棋差不多，只是这个是 3 * 3 的棋盘大小。
A先走，玩的时候规则如下，行、列、斜着三个连到一起就算赢。
那么我们看下如何判断赢呢？
首先行和列通过abs(rows[i])或者abs(cols[j])是否等于3判断，
斜着判断diag_1从左上到右下
斜着判断diag_2从右上到左下
如果都下载完则返回"Draw"，没下完还有空格可以放，则返回"Pending"
"""


class FindWinnerOnATicTacToeGame(object):

    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        diag_1 = diag_2 = 0
        for step, move in enumerate(moves):
            i, j = move
            sign = 1 if step % 2 == 0 else -1
            rows[i] += sign
            cols[j] += sign
            if i == j:
                diag_1 += sign
            if i + j == 3 - 1:
                diag_2 += sign
            if abs(rows[i]) == 3 or abs(cols[j]) == 3 or abs(diag_1) == 3 or abs(diag_2) == 3:
                return "A" if sign == 1 else "B"
        return "Draw" if len(moves) == 3 * 3 else "Pending"


