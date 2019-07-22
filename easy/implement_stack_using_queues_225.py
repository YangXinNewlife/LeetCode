# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这里是一个简单的模拟数据结构Stack栈的一个例子
Stack的结构特点是先进后出。那么
pop()的时候我们只需要处理将集合中的最后一个元素出栈即可；
push()的时候我们追加即可；
top()的时候我们返回最后一个元素即可；
empty()的时候我们判断长度即可；
"""


class ImplementStackUsingQueues(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.stack:
            return self.stack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.stack) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
