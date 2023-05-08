#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #pq = PriorityQueue()
        pq = []
        dummy = ListNode()
        p = dummy
        for i, list in enumerate(lists):
            if not list:
                continue
            #pq.put((list.val, list))
            heapq.heappush(pq, [lists[i].val, i])
        while pq:
            #_, node = pq.get()
            _, i = heapq.heappop(pq)
            node = lists[i]
            tmp = node.next
            node.next = None
            p.next = node
            p = p.next
            if tmp:
                lists[i] = tmp
                heapq.heappush(pq, [tmp.val, i])
                #pq.put((tmp.val, tmp))
        return dummy.next
# @lc code=end

