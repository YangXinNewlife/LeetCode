# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
函数的逻辑是计算元素的乘积，
然后判断大于0，小于0和等于0即可。
这里使用functools的reduce函数可以节省for循环操作
"""
from functools import reduce


class SignOfTheProductOfAnArray(object):

    def arraySign(self, nums: List[int]) -> int:
        temp_result = reduce(lambda x, y: x * y, nums)
        if temp_result > 0:
            return 1
        elif temp_result < 0:
            return -1
        else:
            return 0



