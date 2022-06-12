# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
思考：
题目是要把所有的卡片挪到同一个位子，规则如下：
position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
意思就是左右挪动两个位子消耗为0，左右挪动一个位子消耗为1。
因为 
1 <= position.length <= 100
1 <= position[i] <= 10^9
那么如果循环便套用公式肯定会超时，因为遍历要从最大值到最小值，范围太大了。

解决方案：
我们换一个思路，如果我们只按照消耗一次和消耗两次来分。就可以把数据氛围奇数和偶数。
那么最所有数据会成为两堆，那么只要统计一堆比较少，我们就挪那堆比较少的即可。
计算出小的堆，看下多少个，就是消耗的最少都能挪动为一堆。
"""


class MinimumCostToMoveChipsToTheSamePosition(object):

    def minCostToMoveChips(self, position: List[int]) -> int:
        cnt = 0
        for j in position:
            if j % 2 == 0:
                cnt += 1
        return min(cnt, len(position) - cnt)


