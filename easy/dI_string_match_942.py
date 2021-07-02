# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题目的意思是给出由I和D组成的字符串，其中I开始递减D开始递增，字符串的长度就是数字的个数
例如：IDID -> 0 ～ 4 
题目要求返回任意一组即可，那么我们可以将
第一个出现的 I 的位置对应的是0，
第一个出现的 D 的位置对应的是N，
那么无论这个位置后面出现的是另外哪个数字，
当前的位置都能满足题设条件。
"""


class DIStringMatch(object):

    def diStringMatch(self, s: str) -> List[int]:
        list_len = len(s)
        index_i, index_d = 0, list_len
        result = list()
        for i in s:
            if i == 'I':
                result.append(index_i)
                index_i += 1
            else:
                result.append(index_d)
                index_d -= 1
        result.append(index_i)
        return result

