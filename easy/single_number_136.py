# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
性质一：
交换律 a ^ b = b ^ a，
性质二：
a ^ a = 0。
于是我们可以将所有元素依次做异或操作，相同元素异或结果为0，
因此最终剩下的元素就为Single Number。
异或操作符 a ^ b
"""


class SingleNumber(object):

    def singleNumber(self, nums) -> int:
        """
        根据时间复杂度以及空间复杂度的要求：
        Your algorithm should have a linear runtime complexity.
        Could you implement it without using extra memory?
        这里建议使用位运算的异或操作
        :param nums:
        :return:
        """
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
        return result


