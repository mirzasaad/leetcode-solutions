# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow, fast = ListNode(-1), ListNode(-1)
        slow.next, fast.next = head, head

        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        return slow.next