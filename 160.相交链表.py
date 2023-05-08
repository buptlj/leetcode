#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        p2 = headB
        len_a = 0
        len_b = 0
        while p1:
            p1 = p1.next
            len_a += 1
        while p2:
            p2 = p2.next
            len_b += 1
        p1 = headA
        p2 = headB
        if len_b > len_a:
            for i in range(len_b - len_a):
                p2 = p2.next
        else:
            for i in range(len_a - len_b):
                p1 = p1.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

        
# @lc code=end

