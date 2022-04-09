# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import datetime
"""
Solutions:
题目的意思就是给定'%Y-%m-%d'样式的输入，然后计算出这是一年的多少天，我们直接使用函数即可。
"""


class DayOfTheYear(object):

    def dayOfYear(self, date: str) -> int:
        return int(datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%j'))
