# -*- coding:utf-8 -*-
__author__ = 'yangxin'
"""
Soultions:
题意：
给定一个糖果🍬数组，其中每个数字代表一个糖果的种类，例如：candies = [1,1,2,2,3,3]代表共有三类糖果（1，2，3），
其中糖果的数量一定是偶数的，然后sister可以拿到的数量一定是len(candies) / 2，糖果总数的一半，问sister最多可以拿多少种类；
分析：
那么共有两种可能性，如果sister拿到糖果的数量大于等于糖果的种类，那么sister拿到的就是糖果种类的数量；
如果sister拿到的糖果数量小于糖果的种类数量，那么sister可以拿到的糖果种类数量就是他手里糖果的数量；
"""


class DistributeCandies(object):

    def distributeCandies(self, candies: List[int]) -> int:
        return min(int(len(candies)/2), len(set(candies)))
