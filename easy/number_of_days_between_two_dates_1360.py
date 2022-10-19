# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
import datetime
"""
Solutions:
题目的意思就是计算两个时间的距离，
逻辑可以利用datetime.datetime的方式计算为天，
因此用两个天的变量算差值即可。
"""


class NumberOfDaysBetweenTwoDates(object):

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        year_1, month_1, day_1 = date1[0:4], date1[5:7], date1[8:10]
        year_2, month_2, day_2 = date2[0:4], date2[5:7], date2[8:10]
        days_1 = datetime.datetime(int(year_1), int(month_1), int(day_1))
        days_2 = datetime.datetime(int(year_2), int(month_2), int(day_2))
        return abs((days_1 - days_2).days)
