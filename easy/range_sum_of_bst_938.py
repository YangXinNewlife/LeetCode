# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意：找出一个BST（二叉搜索树，自带排序，left小于root，right大于root）中，计算在[L,R]双闭区间内的所有节点的值的和。
例如：
root = [10,5,15,3,7,null,18], low = 7, high = 15
在区间范围内的有
7 + 10 + 15 return 32
因此我们只需要拆分：
elif low <= root.val <= high:
    计算
elif root.val < low:
    计算
elif root.val > high:
    计算
"""


class RangeSumOfBST(object):

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        result = 0
        if not root:
            return result
        elif low <= root.val <= high:
            result += root.val
            result += self.rangeSumBST(root.left, low, high)
            result += self.rangeSumBST(root.right, low, high)
        elif root.val < low:
            result += self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            result += self.rangeSumBST(root.left, low, high)
        return result
