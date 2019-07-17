# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
1.想达到求两数之和，并且O(n)的情况下。
2.可以设置两个指针，左边界一个，右边界一个。
3.当左右指针之和小于目标数 target, 则向右挪动左指针。
4.当左右指针之和大雨目标数 target, 则向左挪动有指针。
5.当左右指针之和正好等于目标数 target, 则返回指针下标的数目 + 1。
"""


class TwoSumLLInputArrayIsSorted(object):

    def twoSum(self, numbers, target: int):
        """
        双指针解题
        :param numbers:
        :param target:
        :return:
        """
        left = 0
        right = len(numbers) - 1
        ans = [0] * 2
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                ans[0], ans[1] = left + 1, right + 1
                break
        return ans



