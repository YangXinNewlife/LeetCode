# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的思路就是按照指令执行就可以了，就是一个机器人，按照commands方式走路，obstacles是障碍坐标。
-2是向左转，方向计算公式 dir = (dir - 1) % 4
-1是向右转，方向计算公式 dir = (dir + 1) % 4
其余数字正常向前走。每走一次都会有一个移动到（0。0）的最大值（X^2 + y^2）;
"""


class WalkingRobotSimulation(object):

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        offset_tuple = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        obstacles = set(map(tuple, obstacles))
        x, y, dir, max_distance = 0, 0, 0, 0
        for i in commands:
            if i == -2:
                dir = (dir - 1) % 4
            elif i == -1:
                dir = (dir + 1) % 4
            else:
                x_off, y_off = offset_tuple[dir]
                while i:
                    if (x + x_off, y + y_off) not in obstacles:
                        x += x_off
                        y += y_off
                    i -= 1
                max_distance = max(max_distance, x ** 2 + y ** 2)
        return max_distance


