# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是统计一下每个域名（包含子域名）出现的次数；
例如：
["9001 discuss.leetcode.com"]
discuss.leetcode.com 9001次
leetcode.com 9001次
com 9001次
那么我们只需要利用字典dict的数据结构
累加每种域名出现的次数即可
"""


class SubdomainVisitCount(object):

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_dict = dict()
        for i in cpdomains:
            i = i.replace(' ', '.').split('.')
            for j in range(1, len(i)):
                item = '.'.join(i[j:])
                domain_dict[item] = domain_dict.get(item, 0) + int(i[0])
        return [' '.join([str(v), k]) for k, v in domain_dict.items()]
