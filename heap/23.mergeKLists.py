# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = current = ListNode(0)
        q, count = [], 0
        for linked_list in lists:
            if linked_list is not None:
                count += 1
                heapq.heappush(q, (linked_list.val, count, linked_list))
        
        while q:
            _, _, current.next = heapq.heappop(q)
            current = current.next
            if current.next is not None:
                count += 1
                heapq.heappush(q, (current.next.val, count, current.next))
        return head.next