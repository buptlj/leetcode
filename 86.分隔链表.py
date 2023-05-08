#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        p1 = dummy1
        dummy2 = ListNode()
        p2 = dummy2
        while head:
            if head .val < x:
                dummy1.next = head
                dummy1 = dummy1.next
            else:
                dummy2.next = head
                dummy2 = dummy2.next
            head = head.next
        dummy2.next = None # 尾节点next置空，否则可能链接到p1中元素
        dummy1.next = p2.next
        return p1.next

# @lc code=end

