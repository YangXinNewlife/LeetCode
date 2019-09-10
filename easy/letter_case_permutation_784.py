# -*- coding:utf-8 -*-
__author__ = 'yangxin_Ryan'
"""
此处使用回溯 + 深度优先算法DFS
遍历每个字符，如果是字符则索引（index） + 1,
然后将字符分别转换大小写，然后每一个结果子集用path存储。
每一个结果可能性遍历完，怎将结果加入res中。
最后res返回的就是所有的可能性。
"""


class LetterCasePermutation(object):

    def letterCasePermutation(self, S):
        """
        :param S:
        :return:
        """
        res = []
        self.dfs(S, 0, '', res)
        return res

    def dfs(self, s, index, path, res):
        """
        :param s:
        :param index:
        :param path:
        :param res:
        :return:
        """
        if index == len(s):
            res.append(path)
            return
        else:
            if s[index].isalpha():
                self.dfs(s, index + 1, path + s[index].lower(), res)
                self.dfs(s, index + 1, path + s[index].upper(), res)
            else:
                self.dfs(s, index + 1, path + s[index], res)


