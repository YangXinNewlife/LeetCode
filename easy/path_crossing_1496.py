# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目是给定一个移动路线，NSWE，东南西北。如果按照给定的移动路径行走，
有重复走过的点，则返回True，否则返回False。
"""


class PathCrossing(object):

    def isPathCrossing(self, path: str) -> bool:
        path_map = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
        visit_path = set()
        cur_point = (0, 0)
        visit_path.add(cur_point)
        for i, elem in enumerate(path):
            temp_point = (cur_point[0] + path_map[elem][0], cur_point[1] + path_map[elem][1])
            if temp_point in visit_path:
                return True
            else:
                visit_path.add(temp_point)
                cur_point = temp_point
        return False




