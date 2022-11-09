# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是重新格式化字符串后返回
其中主要的操作是返回数字和字符穿插组合两个相同的类型不相连的字符串，
如果没有则返回空字符串
主要的算法设计思路就是
1.先判断是否给出的刚好是一个，则返回
2.将数字和字符进行抽离
3.如果抽离出来的数字和字符个数刚好等于给出的原始字符串长度则代表给出的就是纯字符或者数字。则返回空
4.除上述逻辑外，则可以将字母和数字按照1：1进行规律重排。
zip(list1,list) => 长度较小的那个重排的结果，剩余的再部上去即可，如下：
[a,b,c,d]
[1,2,3]
zip => [(a,1),(b,2),(c,3)]
再补上一个str_list[len(digit_list):
长度较长的剩余字符即可
"""


class ReformatTheString(object):

    def reformat(self, s: str) -> str:
        result = ""
        if len(s) == 1:
            return s
        digit_list = list()
        str_list = list()
        for i in s:
            if i.isdigit():
                digit_list.append(i)
            else:
                str_list.append(i)
        if len(digit_list) == len(s) or len(str_list) == len(s) or abs(len(digit_list) - len(str_list)) > 1:
            return result
        if len(str_list) < len(digit_list):
            str_list, digit_list = digit_list, str_list
        return "".join([i for j in zip(str_list, digit_list) for i in j] + str_list[len(digit_list):])









