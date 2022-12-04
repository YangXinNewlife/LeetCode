# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定 numBottles 个满水瓶，喝光后，剩余的空瓶子可以换满水瓶，
numExchange个空瓶子换一个满水瓶。最后算下一共可以喝几瓶。
通过计算除法计算初始的瓶子和换购后的瓶子得到一共喝几瓶。
"""


class WaterBottles(object):

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles >= numExchange:
            temp_result = numBottles // numExchange
            result += temp_result
            numBottles = numBottles % numExchange + temp_result
        return result
