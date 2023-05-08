#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        # if not root.left:
        #     return self.minDepth(root.right) + 1
        # if not root.right:
        #     return self.minDepth(root.left) + 1
        # return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        q = [root]
        res = 1
        while q:
            tmp = []
            for node in q:
                if not node.left and not node.right:
                    return res
                if node.left: tmp.append(node.left)
                if node.right: tmp.append(node.right)
            res += 1
            q = tmp
        return res
# @lc code=end

