# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是在一个Stream中随机的加入数字，然后返回第K个大的元素；
例如：[4,5,8,2]
k = 3，则返回 4；
add 3, k = 3 则返回 4；
add 5, k = 3 则返回 5；
....
依此类推我们可以看出是计算TopN的最小的元素算法，那么TopN就选择用'堆'来实现，
最小的元素，则使用小顶堆最方便，我们可以维护一个大小为K的堆，因此小顶堆的根就是第K大的元素；
"""

import heapq


class KthLargestElementinAStream(object):
    """
    # Your KthLargest object will be instantiated and called as such:
    # obj = KthLargest(k, nums)
    # param_1 = obj.add(val)
    """

    def __init__(self, k: int, nums):
        self.data = nums
        self.k = k
        self.size = len(nums)
        heapq.heapify(self.data)
        while self.size > k:
            heapq.heappop(self.data)
            self.size -= 1

    def add(self, val: int) -> int:
        if self.size < self.k:
            heapq.heappush(self.data, val)
            self.size += 1
        elif val > self.data[0]:
            heapq.heapreplace(self.data, val)
        return self.data[0]
