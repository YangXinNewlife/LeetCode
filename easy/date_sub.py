# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目：
写一个函数，输入是两个日期，输出是这两个日期的日差。
例如：输入是20190102和20190103，输出是1
要求：
1、不能使用系统自带函数直接减
2、不能使用时间戳
3、日期格式是字符串类似2019-01-02格式，只考虑四位字符年份

解题分析：
此题目由于要求必须不能使用自带的方法，那么我就可以考虑拆分年、月、日分别来计算
那么年份所影响的条件有 闰年 与 非闰年。
因此我们就要分两种情况来考虑：
1.同年 -> 差值为 0；
2.非同年 -> 差值为非 0；
最后分年、月、日计算对应的差值 * 天数即可；
"""


class DateSub(object):

    def is_leap_year(self, year):
        """
        判断是否是闰年
        :param year:
        :return:
        """
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def date_sub(self, date1, date2):
        """
        计算两个日期的差值，考虑是否包含闰年
        :param date1:
        :param date2:
        :return:
        """
        result = 0
        date1 = date1.replace("-", "")
        date2 = date2.replace("-", "")
        temp1 = max(date1, date2)
        temp2 = min(date1, date2)
        date2 = temp1
        date1 = temp2
        date1_year = int(date1[0:4])
        date1_month = int(date1[4:6])
        date1_day = int(date1[6:8])
        date2_year = int(date2[0:4])
        date2_month = int(date2[4:6])
        date2_day = int(date2[6:8])
        if self.is_leap_year(date1_year):
            day_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year_temp = date2_year - date1_year
        month_temp = date2_month - date1_month
        if year_temp == 0:
            if month_temp == 0:
                result = date2_day - date1_day
            else:
                i = 1
                temp_sum = 0
                while i < month_temp + 1:
                    day = day_of_month[date1_month + i - 1 - 1]
                    temp_sum += day
                    i += 1
                result = temp_sum - date1_day + date2_day
        else:
            if self.is_leap_year(date2_year):
                day_of_month2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                year_days = 366
            else:
                day_of_month2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                year_days = 365
            i = 1
            temp_sum1 = 0
            temp_sum2 = 0
            middle_year_sum_days = 0
            while i < date1_month:
                day = day_of_month[date1_month - i - 1]
                temp_sum1 += day
                i += 1
            other_days1 = year_days - temp_sum1 - date1_day
            i = 1
            while i < date2_month:
                day = day_of_month2[date2_month - i - 1]
                temp_sum2 += day
                i += 1
            other_days2 = temp_sum2 + date2_day
            i = 1
            while i < year_temp:
                middle_year = date1_year + i
                if self.is_leap_year(middle_year):
                    year_day = 366
                else:
                    year_day = 365
                middle_year_sum_days += year_day
                i += 1
            result = middle_year_sum_days + other_days1 + other_days2
        return result


if __name__ == '__main__':
    date_sub = DateSub()
    print(date_sub.date_sub("2019-1-25", "2019-1-26"))


