#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        if k == 1: return head
        a = head
        for i in range(k):
            if not a: return head
            a = a.next
        def reverse(head, k):
            if not head or not head.next: return head
            p = None
            cur = head
            for i in range(k):
                tmp = cur.next
                cur.next = p
                p = cur
                cur = tmp
            return p, cur
        p, cur = reverse(head, k)
        head.next = self.reverseKGroup(cur, k)
        return p

# @lc code=end

