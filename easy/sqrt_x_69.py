# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import math


class Sqrt(object):

    def run(self, x):
        """
        求平方根函数
        :param x:
        :return:
        """
        return int(math.sqrt(x))


if __name__ == '__main__':
    sqrt = Sqrt()
    x = 4
    sqrt.run(x)


