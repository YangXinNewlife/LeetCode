# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
1.先反转两个字符串，然后生成为list，这里题目有要求，不能使用库函数直接把string转换为int（自己实现）
2.如果num2长度大于num1的长度，这里的目的是后面循环的时候，用一个比较大的数去循环。
3.声明carry保留进位
"""


class AddStrings(object):

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 反转两个字符串为list
        num1, num2 = list(map(self.convert_int, num1[::-1])), list(map(self.convert_int, num2[::-1]))
        # 根据长度做交换
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        carry = 0
        for i in range(len(num1)):
            n = num2[i] if i < len(num2) else 0 # 位数不够可以补0
            tmp = n + carry + num1[i] # num1与num2对应的位置相加并且带上进位carry
            num1[i] = tmp % 10   # 计算
            carry = tmp // 10    # 保留进位
        if carry:
            num1.append(1)
        # 这里没有要求不能讲int转换为str，所以直接使用了内存函数str()s
        return ''.join(map(str, num1))[::-1]

    def convert_int(self, num):
        """
        将字符转换成为int类型，非内置函数方式
        :param num:
        :return:
        """
        return ord(num) - ord('0')
