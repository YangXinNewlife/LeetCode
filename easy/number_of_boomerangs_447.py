# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意：
给定一组数据 [[0,0],[1,0],[2,0]]，我们以其中一个为中心点，其余的点到这个中心点的距离相等的点组成的列表有几个？
例如上面的例子中符合的是下面两个：
[[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
具体的解决思路是；首先我们用hash或者字典dict存储距离为1的点有多少个，距离为2的点有多少个，距离为3的点有多少个...
这里用距离计算公式来处理：dis_key = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2)
然后
最后我们用 n 个点有多少种两两组合的方式呢？
n * (n - 1)
"""


class NumberOfBoomerangs(object):

    def numberOfBoomerangs(self, points):
        if len(points) < 3:
            return 0
        res = 0
        for i in range(len(points)):
            p_dict = {}
            for j in range(len(points)):
                if j == i:
                    continue
                dis_key = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2)
                if dis_key in p_dict:
                    p_dict[dis_key] += 1
                else:
                    p_dict[dis_key] = 1
            for k in p_dict:
                if p_dict[k] > 1:
                    res += p_dict[k] * (p_dict[k] - 1)
        return res





