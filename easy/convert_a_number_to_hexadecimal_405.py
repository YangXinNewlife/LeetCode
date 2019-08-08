# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
对于输入的num，每次num & 15 可以获取到最右的4个bit位，然后 num >> 4循环处理即可将num转换为16进制。
因为num范围位32bit位，因此最多右移8次，每次右移4个bit位。当num不为0时，
转换位16进制后，前面有0需要去掉。
"""


class ConvertANumberToHexadecimal(object):

    def toHex(self, num):
        """
        题目中的备注信息：
        1.所有16进制字符串中的字符都必须为小写；
        2.16进制字符串不得柏寒额外的前导0。如果数字位零，则由单个零字符'0'表示。
        否则，十六进制字符中的第一个字符将不是零字符；
        3.保证给定数字适合32位有符号整数的范围；
        4.不能使用Python库提供的任何方法将数据直接转换/格式化位十六进制;
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        result = ''
        hex_str = '0123456789abcdef'
        for i in range(8):
            temp = hex_str[num & 15]
            result = temp + result
            num = num >> 4
        return result.lstrip('0')


