# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意先理解很重要，这个是最难的。
我们会给丁一组键值对，其中包含插入的下标索引和对应的元素
如果插入的位置和当前顺序的位置不一致，则返回[]
否则插入的位置和档期那位置一致是，返回包含当前值后面的子数组。
然后将多组子数组，组合到一个二维数组中，并返回。
如下例子：
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
先给定了n的大小，是5
然后插入下标为3-1=2的元素"ccccc",但是当前的操作符在0，因此返回[]
然后插入1-1=0的元素"aaaaa"，当前a后无连续数组，则返回["aaaaa"]
然后插入2-1=1的元素"bbbbb"，当前b后又连续的"ccccc", 则返回["bbbbb","ccccc"]
然后插入5-1=1的元素"eeeee"，当前d后吴涟序序数组，则返回[]
最后插入4-1=3的元素"ddddd"，则返回d后的["ddddd","eeeee"]
"""


class DesignAnOrderedStream(object):
    # Your OrderedStream object will be instantiated and called as such:
    # obj = OrderedStream(n)
    # param_1 = obj.insert(idKey,value)

    """
    def __init__(self, n: int):
        self.result = [None] * n
        self.pre = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.result[idKey - 1] = value
        if self.pre == idKey - 1:
            temp = self.pre
            while temp < len(self.result) and self.result[temp]:
                temp += 1
            self.pre = temp
            return self.result[idKey - 1: self.pre]
        return []
