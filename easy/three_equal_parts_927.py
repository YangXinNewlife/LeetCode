# -*- coding:utf-8 -*-
__author__ = 'yangxin'
"""
Soultions:
* 先统计A中的1的个数one，如果不能被3整除，那么返回[-1,-1]；
* 因为我们如果将A分成相等的三份，那么这三份包含1的个数一定是相同的。如果ones==0，我们返回[0,len(A)-1]；
* 并且[0,i]这个区间内包含ones/3个1，[i+1, j-1]这个区间内包含ones/3个1，最后的区间内包含ones/3个1；
* 最后判断三个区间的数据值是否已知；
* i 在第一个 1 出现的位置，而 j 在第ones/3 + 1个 1 出现的位置；
* 只要判断 A[i]==A[j] and A[j]==A[k]，并且移动指针；
"""


class ThreeEqualParts(object):

    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        one = A.count(1)
        A_len = len(A)
        if not one:
            return [0, A_len - 1]
        if one % 3 != 0:
            return [-1, -1]
        step = one // 3
        index, cnt = [0] * 3, 0
        for i, num in enumerate(A):
            if num == 1:
                if cnt % step == 0:
                    index[cnt // step] = i
                cnt += 1
        while index[2] < A_len and A[index[0]] == A[index[1]] == A[index[2]]:
            index[0] += 1
            index[1] += 1
            index[2] += 1
        if index[2] == A_len:
            return [index[0] - 1, index[1]]
        return [-1, -1]



