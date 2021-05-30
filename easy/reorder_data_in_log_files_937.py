# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions
题意如下
有一组日志。每个日志都是用空格分隔的字符串，其中第一个单词是标识符。
日志有两种类型:
字母日志: 所有单词 (标识符除外) 均由小写英文字母组成。
数字日志: 所有单词 (标识符除外) 均由数字组成。
对这些日志重新排序，以便:
字母日志在所有数字日志之前。
字母日志根据其内容按词典排序。如果它们的内容相同，则根据它们的标识符对它们进行词典排序。
数字日志保持其相对顺序。
返回日志的最终顺序。
知道题意我们就知道需要对排序重新弄，我们把字母和数字分开排序即可。
"""


class ReorderDataInLogFiles(object):

    def sort_function(self, logs):
        identifier, remain_part = logs.split(" ", 1)
        return (0, remain_part, identifier) if remain_part[0].isalpha() else (1, )

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=self.sort_function)
