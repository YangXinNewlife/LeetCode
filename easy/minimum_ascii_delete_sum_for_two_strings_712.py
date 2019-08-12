# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
初始化的是时候我们先将dp[i][0],dp[j][0]初始化位空，
s1需要删除的ascii，也就是s1的前i个字符串的ascii, 
s2需要删除的ascii，也就是s2的前j个字符串的ascii,
当s1[i] == s[j]时，直接将dp[i][j]赋值为dp[i-1][j-1]就行，表示此时添加两个字符(s1[i]、s2[j])对原来的字符串的比较没有影响；
否则，有两种选择,其一，删除s1[i],即原字符串(s1[,i-1]和s2[,j])添加一个字符串s1[i]时，要保持两个两个字符串相同，
就用原字符子串的dp + s1[i], 也就是dp[i-1][j] + ord(s1[i - 1]);
同理，另一个钟就是dp[i][j-1] + ord(s2[j-1])。
取两个值比较小的，就是使当前两个字符子串相同删除的最小ascii值。
"""


class MinimumASCIIDeleteSumForTwoStrings(object):

    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        len1 = len(s1) + 1
        len2 = len(s2) + 1
        dp = [[0] * len2 for i in range(len1)]
        for i in range(1, len2, 1):
            dp[0][i] = dp[0][i - 1] + ord(s2[i - 1])
        for i in range(1, len1, 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
            for j in range(1, len2, 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
        return dp[i][j]
