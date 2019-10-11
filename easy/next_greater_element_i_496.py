# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Soultions:
题意是第一个数组是第二个数组的子数组。
找到第一个数组中数字在第二个数组中下一个比它大的元素，如果没有返回-1。
下面的代码时使用stack的远离来实现，先将全集nums2中的每个元素i，找到比i的大元素。
然后最后只需要判断子集中每个元素在dict中是否有记录（即是否有比它大的数据即可，没有则赋值-1，有则填充）。
"""


class NextGreaterElementI(object):

    def nextGreaterElement(self, nums1, nums2):
        dic, stack = {}, []
        for i in nums2:
            while stack and stack[-1] < i:
                dic[stack.pop()] = i
            stack.append(i)
        return [dic.get(j, -1) for j in nums1]
