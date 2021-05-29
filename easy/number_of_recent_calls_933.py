# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
想要做出来首先要理解题意，
题目的意思是写一个 RecentCounter 类来计算最近的请求。
它只有一个方法：ping(int t)，其中 t 代表以毫秒为单位的某个时间。
返回从 3000 毫秒前到现在的 ping 数。
任何处于 [t - 3000, t] 时间范围之内的 ping 都将会被计算在内，包括当前（指 t 时刻）的 ping。
保证每次对 ping 的调用都使用比之前更大的 t 值。
因此我们只需要维护一个[t - 3000, t]的窗口就可以了，每次计算下，在该区间内的就加进去，否则不用。
那么我们可以用队列来模拟窗口实现。
[1]           [-2999, 1]       包含 1               返回 1 个
[100]         [-2900, 100]     包含 1、100          返回 2 个
[3001]        [1, 3001]        包含 1、100、3001    返回 3 个
[3002]        [2, 3002]        包含 2、100、3002    返回 3 个
"""


class RecentCounter:

    def __init__(self):
        self.queue = list()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < (t - 3000):
            self.queue.pop(0)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
