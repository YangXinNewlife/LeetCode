# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
题目的大概含义：
给你一个数组，里面的字符串包含每轮的得分，还有其余对得分的操作：
Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
我们只需要遍历这些每个输入的元素，然后新开一个空间存储每次处理的结果即可，由于存在"C",remove操作，我这里使用可以支持出栈的stack(实际还是list)来处理；
* 当遇到 "+": 我们就把前两个数据求和放到当前下标的元素位置；
* 当遇到 "D": 我们就把前一个数据乘二放到当前下标的元素位置；
* 当遇到 "C": 我们就把前一个数据remove，这里使用出栈的方式；
* 当遇到 "得分": 我们就把前数据追加到集合的当前下标的元素位置；
最后返回这个集合的sum值即可；
"""


class BaseballGame(object):

    def calPoints(self, ops: List[str]) -> int:
        result_stack = []
        for i in ops:
            if i == "+":
                result_stack.append(result_stack[-1] + result_stack[-2])
            elif i == "C":
                result_stack.pop()
            elif i == "D":
                result_stack.append(result_stack[-1] * 2)
            else:
                result_stack.append(int(i))
        return sum(result_stack)

