# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
Solution-1:
可以做下暴力算法的提效，
每次便利固定b和c的位置，直接可以推断出来a和d的活动范围。
b固定后，c = b + 1
最后只需要遍历a和d即可

Solution-2:
使用暴力的解法直接四个for遍历题意说明的循环，模拟操作，
枚举所有的可能性。

"""


class CountSpecialQuadruplets(object):

    def countQuadruplets(self, nums: List[int]) -> int:
        nums_len = len(nums)
        result = 0
        nums_dict = dict()
        for b in range(nums_len - 3, 0, -1):
            for d in range(b + 2, nums_len):
                nums_dict[nums[d] - nums[b + 1]] = nums_dict.get(nums[d] - nums[b + 1], 0) + 1
            for a in range(0, b):
                result += nums_dict.get(nums[a] + nums[b], 0)
        return result


    def countQuadruplets(self, nums: List[int]) -> int:
        nums_len = len(nums)
        result = 0
        for a in range(nums_len - 3):
            for b in range(a + 1, nums_len - 2):
                for c in range(b + 1, nums_len - 1):
                    for d in range(c + 1, nums_len):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            result += 1
        return result

