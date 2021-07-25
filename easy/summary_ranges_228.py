# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目就是很明显的区间合并问题，这里的考虑
方法是判断下当前元素和后一个元素的值是否相差 1,
就把这个相差 1 的连续两个元素, 按照结果输出要求 %s->%s 放进结果集合（连续的最后一个，在while j < len(nums) - 1 and nums[j] == nums[j + 1] - 1:中体现作用），
如果后者没有相差 1，那么则单独把元素放进去。
总结：
单独不连续放当前元素；
连续放当前和后一个元素；

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""


class SummaryRanges(object):

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums is None:
            return nums
        result = list()
        i = 0
        while i < len(nums):
            j = i
            while j < len(nums) - 1 and nums[j] == nums[j + 1] - 1:
                j += 1
            if j == i:
                result.append(str(nums[i]))
            else:
                result.append('%s->%s' % (nums[i], nums[j]))
            i = j + 1
        return result

