#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        if left == right: return head
        dummy = ListNode(0, head)
        pre = dummy
        cur = head
        next = head.next
        for i in range(1, left):
            pre = pre.next
            cur = cur.next
            next = next.next
        for i in range(right - left):
            cur.next = next.next
            next.next = pre.next
            pre.next = next
            next = cur.next
        return dummy.next


# @lc code=end

