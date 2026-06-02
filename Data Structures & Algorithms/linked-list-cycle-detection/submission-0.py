# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's fast-and-slow algorithm for cycle detection
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next # must exist
            fast = fast.next.next
            if slow == fast: # compares NODES, not values
                return True
        return False