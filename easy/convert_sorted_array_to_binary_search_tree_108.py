# -*- coding:utf-8 -*-
__author__='yangxin_ryan'
"""
Solutions:
解题思路主要还是先理解题意，首先什么是BST以及什么是高度平衡树。
* 二叉查找树（Binary Search Tree），（又：二叉搜索树，二叉排序树）它或者是一棵空树，或者是具有下列性质的二叉树：若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；它的左、右子树也分别是二叉排序树。
* 平衡二叉树（Self-Balancing Binary search Tree）又被称为 AVL（三个人名首字母） 数，且具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1。

然后难点来了，怎么把数组输入建树呢？
1. 找到“最中间”的位置取一个根结点：为了确保高度差绝对值小于等于 1，我们需要找到最中间的位置取根结点，于是这里就取出了 3。
2. 以根结点为中心，划分从数组开始到根结点结束的左侧数组（根结点的左子树数据），以及从根结点开始到原数组结束为止的右侧数组（根结点的右子树数据）。
   于是，这里出现的左子树数组就是 [1, 2]，右子树数组就是 [4, 5]
3. 我们重复第 1 步的操作，在左子树数组中找到了我们认为的“最中间”的位置 ；然后我们又重复了第 2 步的操作，将该左子树数组划分成了左右两个数组。
   于是，这里我们取到的第二个根结点就是 [2]，划分出来的左右数组为 [1] []
4. 我们一直这样重复下去，依次构造结点的左右子结点指针指向，直到所有的元素都被我们取完结束，此时也就构造出来了被转换成功的高度平衡的二叉搜索树了。
5. 最后总结的规律就是中位数为根节点，中位数左边为左子树，右边为右子树，再继续向下递归拆分。

推演过程：
输入为：[-10,-3,0,5,9]
首先选 0 为根 然后[-10, -3]化为左子树，[5, 9]化为右子树；
然后在左子树中选-3为根，-10为其左子树，左子树建树完毕；
然后再右子树中选9为根，5为其左子树，右子树建树完毕。

"""


class ConvertSortedArrayToBinarySearchTree(object):

    def sortedArrayToBST(self, nums):
        """
        Definition for a binary tree node.
        class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
        :param nums:
        :return:
        """
        size = len(nums)
        if size == 0:
            return None
        if size == 1:
            return TreeNode(nums[0])
        size //= 2
        root = TreeNode(nums[size])
        root.left = self.sortedArrayToBST(nums[:size])
        root.right = self.sortedArrayToBST(nums[size + 1:])
        return root
