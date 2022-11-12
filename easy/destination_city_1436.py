# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一组可联通的路径，
然后判断哪个城市是最终的目的地，
我们可以先统计每个城市的出度和入度。
最后返回只有入度没有出度即可。
"""
import collections


class DestinationCity(object):

    def destCity(self, paths: List[List[str]]) -> str:
        city_in = collections.defaultdict(int)
        city_out = collections.defaultdict(int)
        for i, j in paths:
            city_in[i] += 1
            city_out[j] += 1
        for k in city_out.keys():
            if k not in city_in.keys():
                return k
