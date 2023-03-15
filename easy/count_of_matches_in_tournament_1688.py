# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给出一个数n，判断n是奇数还是偶数
偶数的话继续除2，直到除尽即可。
奇数的话继续+1再除以2，直到除尽。
累加过程结果n即可，直接打表实现
"""


class CountOfMatchesInTournament(object):

    def numberOfMatches(self, n: int) -> int:
        result = 0
        while n > 1:
            result += n // 2
            if n % 2 == 0:
                n = n // 2
            else:
                n = n // 2 + 1
        return result

