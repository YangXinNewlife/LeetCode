# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
首先将加热器的由低到高排序，
然后循环遍历每一个房子的位置，
依次去找比当前房大的加热器，然后去比较当前房子到当前加热器以及比当前大的加热器与当前房子的差值最小，
也就是去找两个极点。
最后在比较已存在的半径大小，找一个大的覆盖所有。
"""


class Heaters(object):

    def findRadius(self, houses, heaters):
        heaters.sort()
        heaters = [float('-inf')] + heaters + [float('inf')]
        radius = count = 0
        for i in sorted(houses):
            while i > heaters[count + 1]:
                count += 1
            dis = min(i - heaters[count], heaters[count + 1] - i)
            radius = max(radius, dis)
        return radius