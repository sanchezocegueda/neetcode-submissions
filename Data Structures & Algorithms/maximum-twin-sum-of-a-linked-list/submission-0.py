# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head # 0
        fast = head # 1

        # step 1: find middle
        while fast.next and fast.next.next:
            
            fast = fast.next.next
            slow = slow.next

        # step 2: reverse second half
        rev_head = slow.next
        prev = None

        while rev_head:
            nxt = rev_head.next
            rev_head.next = prev
            prev = rev_head
            rev_head = nxt

        first_half = head
        second_half = prev
        maxSum = 0
        while second_half:
            maxSum = max(first_half.val + second_half.val, maxSum)
            first_half = first_half.next
            second_half = second_half.next
        
        return maxSum


        
