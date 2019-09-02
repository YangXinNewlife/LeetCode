# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
目的是要求出来没有在这个数据范围内的数据，那么我们可以使用Hash算法。
但是题目要求不能使用多余的额外空间，于是我们想一下有没有更好的办法。
我们可以使用"正负号标记法"
1.遍历数组nums，记当前元素为i，令nums[abs(i) - 1] = -abs(nums[abs(i) - 1]),前移一位，并且求负数。
2.再次遍历nums，将正数对应的下标+1返回即为答案，因为正数对应的元素没有被上一步骤标记过。
"""


class FindAllNumbersDisappearedInAnArray(object):

    def findDisappearedNumbers(self, nums):
        """
        正负号标记法
        :param nums:
        :return:
        """
        for i in nums:
            nums[abs(i) - 1] = -abs(nums[abs(i) - 1])
        return [j + 1 for j, i in enumerate(nums) if i > 0]
