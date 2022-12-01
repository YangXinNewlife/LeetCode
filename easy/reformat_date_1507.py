# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
题目的意思是给定一个字符串，我们要把字符串格式的日期转换为日常的数字格式日期。
月份的话需要做一个词典来处理。
month_dict = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
日比较好处理，利用re的正则表达式查找，找到里面的所有数字即可，年不用处理，左后拼接即可。
"""
import re


class ReformatDate(object):

    def reformatDate(self, date: str) -> str:
        month_dict = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        day, month, year = date.split()
        month = month_dict.index(month) + 1
        if month < 10:
            month = "0" + str(month)
        day = re.findall("\d+", day)[0]
        if int(day) < 10:
            day = "0" + day
        return str(year) + "-" + str(month) + "-" + str(day)


