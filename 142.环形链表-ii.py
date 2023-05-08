#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        i = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            i += 1
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
        
# @lc code=end

