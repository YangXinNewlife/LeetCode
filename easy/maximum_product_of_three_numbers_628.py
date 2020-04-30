# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
题目的要求就是求数组中三个数乘积的最大值，输入有可能存在负值，因此只有三个数都是正数或者只有两个负数的时候才能得到结果是正的，这样我们得到：
1.最右边三个正数或者
2.最左边两个负数和最右边的一个正数
比较两个哪个大就可以了！
"""


class MaximumProductOfThreeNumbers(object):

    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

