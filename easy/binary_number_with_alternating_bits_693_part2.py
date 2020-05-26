# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
part1处理的方式太简单了，有点偷懒，所以写一个手动十进制转二进制方法，即可，然后去判断两个是否相同即可；
相同则说明是00或者11，数据不间隔；
"""


class BinaryNumberWithAlternatingBits(object):

    def hasAlternatingBits(self, n: int) -> bool:
        result_str = ""
        if n == 1:
            return True
        while n:
            result_str += str(n % 2)
            n //= 2

        for i in range(1, len(result_str)):
            if result_str[i] == result_str[i - 1]:
                return False
        return True
