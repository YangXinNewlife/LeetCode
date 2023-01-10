# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是构造一个停车系统的两个函数
1.构造函数
做初始化
2.停车动作系统
对现有的车位做减法
"""
import collections


class DesignParkingSystem(object):
    # Your ParkingSystem object will be instantiated and called as such:
    # obj = ParkingSystem(big, medium, small)
    # param_1 = obj.addCar(carType)

    def __init__(self, big: int, medium: int, small: int):
        self.parking = collections.defaultdict(int)
        self.parking['1'] = big
        self.parking['2'] = medium
        self.parking['3'] = small

    def addCar(self, carType: int) -> bool:
        if 1 == carType:
            self.type = '1'
        elif 2 == carType:
            self.type = '2'
        elif 3 == carType:
            self.type = '3'
        if self.parking[self.type] > 0:
            self.parking[self.type] -= 1
            return True
        else:
            return False

