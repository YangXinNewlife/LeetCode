# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
看到题目理解清晰就很简单，题目的意思是计算树的高度；
这里我们使用深度搜索即可，遍历每一个节点的孩子节点的最大高度再加上根的高度 1 即可。
"""


class MaximumDepthOfNaryTree(object):

    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        depth = 1 + max(self.maxDepth(i) for i in root.children)
        return depth



