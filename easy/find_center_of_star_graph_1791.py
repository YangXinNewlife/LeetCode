# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
因为题目是要找出图的中心，那么中心的定义就是每个节点的边
都与这个中心点有连结，那么只需要判断出来哪个节点的连结是2就可以，
不用再多余的判断
"""


class FindCenterOfStarGraph(object):

    def findCenter(self, edges: List[List[int]]) -> int:
        result_dict = dict()
        for i in edges:
            if i[0] not in result_dict:
                result_dict[i[0]] = 1
            else:
                result_dict[i[0]] += 1
            if result_dict[i[0]] == 2:
                return i[0]
            if i[1] not in result_dict:
                result_dict[i[1]] = 1
            else:
                result_dict[i[1]] += 1
            if result_dict[i[1]] == 2:
                return i[1]
        return -1

