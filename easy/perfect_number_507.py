# -*- coidng:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这道题的思路是对于2，满足条件，则28/2=14也满足条件，4满足条件，则28/4也满足条件。
所以可以对数字从2到sqrt(num)进行查看，如果满足取模运算为0，
则把这个数和num除以这个数的值放到sum里面去。判断是否和num相等即可。
"""


class PerfectNumber(object):

    def checkPerfectNumber(self, num: int) -> bool:
        total, div = 1, 2
        while div * div < num:
            if num % div == 0:
                total += div
                if div * div != num:
                    total += num / div
            div += 1
        return 1 < total == num







