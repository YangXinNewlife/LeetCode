# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意就是统计除了禁止词banned外出现最多的字符串，看着比较好处理，
但是题目下面有提示：
paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
说明除了空格还有这么多，那么我们就得处理成统一格式，然后利用split来转化成为数组。
那么我们利用正则的
p = re.compile(r"[!?',;.]")
方式变成可以使用正则的对象
并且使用sub_paragraph = p.sub(' ', paragraph.lower())将[!?',;.]都变成空格字符串" "。
然后使用collections.Counter统计每个字符串出现的次数，或者使用Hash方式自己实现也可以。
其中count.most_common(1)中的1是返回的是出现最多的，value = [('ball', 2)]
因此，取出 ball 的话就得使用 count.most_common(1)[0][0]。
"""

import re
import collections


class MostCommonWord(object):

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = re.compile(r"[!?',;.]")
        sub_paragraph = p.sub(' ', paragraph.lower())
        words = sub_paragraph.split(' ')
        words = [word for word in words if word and word not in banned]
        count = collections.Counter(words)
        return count.most_common(1)[0][0]
