# -*- coding:utf-8 -*-
__author_ = 'yangxin_ryan'
"""
Solutions:
直接通过判断给出的所有元素是否在给出的三个数组中，至少出现2次
这里给出数据范围是1道100，直接遍历判断即可。
"""


class TwoOutOfThree(object):

    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result = list()
        nums1_list = set(nums1)
        nums2_list = set(nums2)
        nums3_list = set(nums3)
        cnt = 0
        for i in range(1, 101):
            if i in nums1_list:
                cnt += 1
            if i in nums2_list:
                cnt += 1
                if cnt >= 2:
                    result.append(i)
                    cnt = 0
                    continue
            if i in nums3_list:
                cnt += 1
                if cnt >= 2:
                    result.append(i)
            cnt = 0
        return result
