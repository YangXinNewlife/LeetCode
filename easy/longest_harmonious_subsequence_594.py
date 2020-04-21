# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
根据题目我们可以看出来，找到最和谐的子串，我们根据实例：
input:[1,3,2,2,5,2,3,7]
output:5
reason:[3,2,2,2,3]
我们可以看出来只需要找相邻的差值为1的数据对即可，因此我们可以利用Hash的原理，将数据的每个数据分别统计，
然后去查相邻的数据是在数列中存在，并且找出两个数据的数量最大的即可；
公式如下
result = max(result, count[i] + count[i + 1]))
"""


class LongestHarmoniousSubsequence(object):

    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        result = 0
        count = Counter(nums)
        for i in count.keys():
            if i + 1 in count:
                result = max(result, count[i] + count[i + 1])
        return result

