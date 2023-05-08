#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #双指针
        #pre = None
        #cur = head
        #while cur:
        #    tmp = cur.next
        #    cur.next = pre
        #    pre = cur
        #    cur = tmp
        #return pre

        # 递归
        if not head or not head.next:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res

# @lc code=end

