# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这里是用数学公式解决问题
从（0，0）到（m-1,n-1）一共要走m - 1次向下，n-1次向右。也就是在n + m - 2次中选出m-1次向下，也就是C（m + n - 2, m-1）
时间复杂度是O(m + n)，空间复杂度是O(1)。
"""


class UniquePaths(object):
    def uniquePaths(self, m, n):
        """

        :type m: int
        :type n: int
        :rtype: int
        """
        total = m + n - 2
        v = n - 1
        def permutation(m, n):
            son = 1
            for i in range(m, m - n, -1):
                son *= i
            mom = 1
            for i in range(n, 0, -1):
                mom *= i
            return son / mom
        return permutation(total, min(v, total -v))


