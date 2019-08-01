# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这里使用动态规划的方法解决：
拆分大问题：
每一个当前点可能的来源是左边和上边的点，因此我们有公式：
dp[i][j] = dp[i-1][j] + dp[i][j-1]
因此我们只需要累加所有的路径的可能性即可。
"""


class UniquePaths(object):
    def uniquePaths(self, m, n):
        """
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * m for i in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]


