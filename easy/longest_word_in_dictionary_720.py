# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
此题目的含义就是找出给定的数组中的元素的前缀在给定的元素中，最大长度的元素；
如果有相同的元素，则返回字典序最小的那个；
那么这里我们使用的处理方法如下：
1.为了方便遍历的时候查找元素的前缀，我们可以先根据元素的长度对输入的数组排序：sorted(words, key=lambda x: len(x))，
  并且用第一个空元素站位，这里为什么在2中解释；
2.怎么看前一个元素是否时候一个元素的前缀呢？
temp_1 = 'aa'
temp_2 = 'aab'
这里我们使用temp_2[:-1]的方式可以获取到一个左闭右开的区间，就是 'aab' 去掉最后一个开就是 'aa'；
3.最后当我们使用有多个同长度的元素，例如 apple, appla, apply的时候，题目要求返回appla，这种字典序最小的元素。
我们就可以利用sort先排序和max(sorted(pre_result), key=lambda x: len(x))的作用，
首先sorted(pre_result)这种的话，就是先排序，然后我们得到appla, apple, apply;
然后我们再使用max(, key=key=lambda x: len(x))，我们根据长度排序找最大值，但是这里的长度都为5，都是最大值！
那么就默认返回第一个元素，毕竟max函数的返回只有一个！
"""


class LongestWordInDictionary(object):

    def longestWord(self, words: List[str]) -> str:
        pre_result = ['']
        for i in sorted(words, key=lambda x: len(x)):
            if i[:-1] in pre_result:
                pre_result.append(i)
        return max(sorted(pre_result), key=lambda x: len(x))