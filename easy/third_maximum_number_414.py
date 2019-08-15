# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
做这道题目之前本打算用K大数，后来又看了一下，三个变量处理一下就可完成。
我们先定义 a, b, c分别为数据中最大的三位数。并且有以下判断：
1.i > a:
说明数据最大，则赋值给最大的a,其余的数据向后移，并抛弃最后一个数字, a, b, c = i, a, b；
2.a > i > b:
说明数据的大小处于第一大与第二大之间，我们把后两个数据向后移并抛弃最后一个数字，b, c = i, b；
3.b > i > c:
说明数据大小处于第三大，则我们直接赋值c变量即可，c = i；
4.重复的数据直接抛弃，不去移动；
"""


class ThirdMaximumNumber(object):

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = c = None
        for i in nums:
            if i > a:
                a, b, c = i, a, b
            elif a > i > b:
                b, c = i, b
            elif b > i > c:
                c = i
        return c if c is not None else a
