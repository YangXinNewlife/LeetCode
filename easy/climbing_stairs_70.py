# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""


class ClimbingStairs(object):

    def run(self, n):
        """
        解题思路是分析每一个台阶有几种走法，首先，台阶i都可以由i-1的台阶迈一步和i-2的台阶迈两步到达，
        其实除了第一个与第二个台阶以外，都是类似的情况，因此我们可以将迈台阶的步骤拆分成如下：
        n <= 1 dp(0) = 1
               dp(1) = 1
        n > 1  dp(i) = dp(i - 1) + dp(i - 2)
        :param n:
        :return:
        """
        if n <= 1:
            return 1
        result = list()
        result.append(1)
        result.append(1)
        for i in range(2, n + 1):
            result.append(result[i-1] + result[i-2])
        return result[n]



