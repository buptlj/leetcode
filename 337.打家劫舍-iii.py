#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.memo = {}
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right: return root.val
        # return two value, 0: not rob root; 1: rob root
        def dp(node):
            if not node: return (0, 0)
            if not node.left and not node.right: return (0, node.val)
            left = dp(node.left)
            right = dp(node.right)
            # rob root
            res1 = node.val + left[0] + right[0]
            # not rob root
            res2 = max(left[0], left[1]) + max(right[0], right[1])
            return (res2, res1)
        res = dp(root)
        return max(res) 
# @lc code=end

