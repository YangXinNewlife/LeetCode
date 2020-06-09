# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是为了设计一个HashSet，
那么我们可以利用set的特性，底层存储直接初始化为Set(),然后利用set的特性使用
add
remove
in
等判断实现
"""


class DesignHashSet(object):
    """
    # Your MyHashSet object will be instantiated and called as such:
    # obj = MyHashSet()
    # obj.add(key)
    # obj.remove(key)
    # param_3 = obj.contains(key)
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = set()

    def add(self, key: int) -> None:
        self.hashset.add(key)

    def remove(self, key: int) -> None:
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.hashset:
            return True
        else:
            return False

