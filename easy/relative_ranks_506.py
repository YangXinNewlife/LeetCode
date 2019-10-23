# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
这里的处理办法是先将数据排序，默认的前三个元素分别是：
Gold Medal
Silver Medal
Bronze Medal
后面的用下标 + 1代替
"""


class RelativeRanks(object):

    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        pos = {n: i + 1 for i, n in enumerate(sorted(nums, reverse=True))}
        def func(x):
            if pos[x] == 1:
                return "Gold Medal"
            elif pos[x] == 2:
                return "Silver Medal"
            elif pos[x] == 3:
                return "Bronze Medal"
            else:
                return str(pos[x])
        return map(func, nums)





