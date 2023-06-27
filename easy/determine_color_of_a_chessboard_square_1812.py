# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是基于给定的固定国际象棋棋盘，
判断某一个坐标的颜色是黑色还是白色
直接判断横轴x和纵轴y的和是不是奇数即可，
否书直接就是黑色，奇数就是白色。
"""


class DetermineColorOfAChessboardSquare(object):

    def squareIsWhite(self, coordinates: str) -> bool:
        x = coordinates[0]
        y = coordinates[1]
        if (ord(x) - ord('a') + 1 + int(y)) % 2 != 0:
            return True
        else:
            return False



