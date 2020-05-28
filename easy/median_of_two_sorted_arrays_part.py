# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
此题目要求的时间复杂复杂度较小O(logN), 单一扫描完任何一个数组都O(N),
因此我们应该想到利用二分的思想，我们对于每个数组设定三个指针（left, mid, right）
然后因为两个数组相同，因此while arr1_left < arr1_right即可；
然后当判断到两个中位数相同时，则返回即可。
否则进入判断逻辑：
1.首先判断两个数组的个数是奇数还是偶数；
2.当个数是偶数的时候，nums1[arr1_mid] > nums2[arr2_mid]的时候说明，
中位数的区域在nums1[arr1_mid + 1, arr1_right] 和 nums2[arr2_left, arr2_mid]中, 然后继续判断向区间内扫；描
3.当个数是奇数的时候，nums1[arr1_mid] < nums2[arr2_mid]的时候说明，
中位数的区域在nums1[arr1_mid, arr1_right] 和 nums2[arr2_left, arr2_mid]中, 然后继续判断向区间内扫描；
4.直到满足条件 arr1_left < arr1_right退出while或者是 nums1[arr1_mid] == nums2[arr2_mid]返回结果'

模拟过程：
nums1: 1 2 3 4 5 
nums2: 3 4 5 6 7
-- 第一轮  arr1_left = 0, arr1_right = 4; arr2_left = 0, arr2_right = 4; arr1_left < arr1_right;
arr1_mid = 2
arr2_mid = 2
odd_or_even = 1
nums1[arr1_mid]=3 < nums2[arr2_mid]=5
arr1_left = 2 + 1
arr2_right = 2
-- 第二轮  arr1_left = 3, arr1_right = 4; arr2_left = 0, arr2_right = 2; arr1_left < arr1_right;
arr1_mid = 3
arr2_mid = 1
odd_or_even = 0
nums1[arr1_mid]=4 = nums2[arr2_mid]=4
-- 轮次结束
两个数组的中位数是4
"""


class MedianOfTwoSortedArrays(object):

    def find_median(self, nums1, nums2):
        if nums1 is None or nums2 is None or len(nums1) != len(nums2):
            raise Exception
        arr1_left = 0
        arr1_right = len(nums1) - 1
        arr2_left = 0
        arr2_right = len(nums2) - 1
        while arr1_left < arr1_right:
            arr1_mid = (arr1_left + arr1_right) // 2
            arr2_mid = (arr2_left + arr2_right) // 2
            odd_or_even = (arr1_right - arr1_left + 1) % 2 == 0 if 1 else 0
            if nums1[arr1_mid] == nums2[arr2_mid]:
                return nums1[arr1_mid]
            elif nums1[arr1_mid] > nums2[arr2_mid]:
                arr2_left = arr2_mid + odd_or_even
                arr1_right = arr1_mid
            else:
                arr1_left = arr1_mid + odd_or_even
                arr2_right = arr2_mid
        return min(nums1[arr1_left], nums2[arr2_left])


if __name__ == '__main__':
    obj = MedianOfTwoSortedArrays()
    print(obj.find_median([1, 2, 3, 4], [3, 4, 5, 6]))

