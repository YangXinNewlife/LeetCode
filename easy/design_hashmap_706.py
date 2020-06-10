# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
实现hashmap
我们使用dict字典模拟即可
"""


class DesignHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = dict()

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.hash_map.__contains__(key):
            return self.hash_map[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if self.hash_map.__contains__(key):
            self.hash_map.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)