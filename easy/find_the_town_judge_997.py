# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意：
在一个城镇中，有n个人被标记为1到n。有传言说这些人中的一个人是镇上的法官。
我们要找出镇上的法官。
如果城镇法官存在，那么:
1.镇法官不信任任何人。
2.每个人 (除了城镇法官) 都信任城镇法官。
3.只有一个人满足属性1和属性2。
您将获得一个数组信任，其中trust[i] = [ai，bi] 表示标记为ai的人信任标记为bi的人。
如果城镇法官存在并且可以被识别，返回城镇法官的标签，否则返回-1。
那么我们就利用条件
in_degress[j] == 0 and out_degress[j] == n - 1: 判断条件 1和2
我们把每个人 1 ～ n，转化成为数组的序号0 ～ n - 1 方便计算。 
就是统计每个人相信的个数，满足每个人都信任的就是法官。
"""


class FindTheTownJudge(object):

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_degress = [0] * n
        out_degress = [0] * n
        for i in trust:
            in_degress[i[0] - 1] += 1
            out_degress[i[1] - 1] += 1
        for j in range(n):
            if in_degress[j] == 0 and out_degress[j] == n - 1:
                return j + 1
        return -1
