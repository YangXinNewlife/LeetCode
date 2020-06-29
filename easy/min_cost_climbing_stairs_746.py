# -*- coding:utf-8 -*-
__authr__ = 'yangxin_ryan'
"""
Solutions:
题目根普通的爬楼梯很像，但是这个最多就是加了一个权值，每一步都有cost[i]，并且我可以从第零个或者第一个台阶走，然后每一步可以跨过 1 或者 2 个台阶；
最后看如何走完楼梯消耗cost最少，也就是选择的走；
例如：
[10, 15, 20]
共三个台阶
那么我从第零个开始那么就是（10 + 后面选择要走的）
那么我从第一个开始那么就是（15 + 后面选择要走的）
那么这里就有两种情况：走/不走
可以使用动态规划来做,我的第 i 个台阶可以由我的第 i - 1,或者第 i - 2台阶走来，我们为了追求sum(cost[i])最小，则有
dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]) 
"""


class MinCostClimbingStairs(object):

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp.append(0)
        if len(cost) == 1:
            return cost[0]
        if len(cost) == 2:
            return min(cost)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]