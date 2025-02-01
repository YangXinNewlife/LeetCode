# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solution:
题目其实不是很好理解，英文对中文太绕了。
这里简单解读下，给定一个字符串数组nums，和一个目标数字Key,其中我们要定义几个概念：
目标值：key要求在给定的数组nums中存在。然后我们要统计出了key之后的元素这里从i + 1开始，
首先 i + 1 小于给定的长度，这里原本要求是 i < 0 <= i <= nums.length - 2,
那么我们要把所有符合条件的元素重组存起来
0 <= i <= nums.length - 2,
nums[i] == key and,
nums[i + 1] == target.
那么生成新的nums_list_filter，
直接对nums_list_filter便利统计（再利用上面三个条件过滤），选出来出现次数最多的即可。
"""

import collections
class MostFrequentNumberFollowingKeyInAnArray(object):

    def mostFrequent(self, nums: List[int], key: int) -> int:
        nums_list_filter = dict()
        for i in range(len(nums)):
            if nums[i] == key and i + 1 < len(nums):
                if nums[i + 1] in nums_list_filter:
                    nums_list_filter[nums[i + 1]] += 1
                else:
                    nums_list_filter[nums[i + 1]] = 1
        max_cnt = max(nums_list_filter.values())
        num_collect = collections.Counter(nums_list_filter)
        for j, k in num_collect.items():
            if max_cnt == k:
                return j

