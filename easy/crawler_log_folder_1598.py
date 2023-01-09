# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意是给定一系列文件夹操作，
计算我们会到原本的目录要做几步？
其实就是计算下一共运行了几次（原目录不用操作，不计数）
"""


class CrawlerLogFolder(object):

    def minOperations(self, logs: List[str]) -> int:
        result = list()
        for i in logs:
            if "../" == i:
                if len(result) > 0:
                    result.pop()
            elif "./" == i:
                continue
            else:
                result.append(i)
        return len(result)
