# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # slow-fast approach

        slow, fast = head, head

        # step 1: find middle of linked list
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        rev = slow.next
        slow.next = None # prevent cycles

        # step 2: reverse linked list in middle
        prev = None
        while rev:
            nxt = rev.next
            rev.next = prev
            prev = rev
            rev = nxt


        # step 3: merge lists
        rev = prev
        cur = head
        i = 0
        while rev:
            tmp1 = cur.next
            tmp2 = rev.next

            cur.next = rev
            rev.next = tmp1

            cur = tmp1
            rev = tmp2
        
        return
