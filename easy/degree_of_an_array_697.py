# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题义是：先找出包含数量最多的值的子数组,返回最短的子数组长度.如上面例子,数量最多的数是1和2,包含1数字的子数组长度为5,包含2数字的子数组长度为2,所以返回2；
解题方法的话可以利用Hash思想，统计每个元素出现的词次数，然后找到最大值。然后再去判断数据出现的在数组中的下标，
根据下标的出现次数（第一次，最后一次）计算出来最小的子串即可；
"""


class DegreeOfAnArray(object):

    def findShortestSubArray(self, nums) -> int:
        left_nums, right_nums, count_nums = {}, {}, {}
        for i, j in enumerate(nums):
            if j not in left_nums:
                left_nums[j] = i
            right_nums[j] = i
            count_nums[j] = count_nums.get(j, 0) + 1
        result = len(nums)
        degree = max(count_nums.values())
        for k in count_nums:
            if count_nums[k] == degree:
                result = min(result, right_nums[k] - left_nums[k] + 1)
        return result


if __name__ == '__main__':
    degree_of_an_array = DegreeOfAnArray()
    print(degree_of_an_array.findShortestSubArray([1,3,2,2,3,1]))




