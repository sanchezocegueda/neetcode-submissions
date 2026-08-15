# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        

        # step 1: add numbers
        dummy = ListNode(-1)
        carry = 0
        curNode = dummy

        while l1 is not None and l2 is not None:
            newVal = (l1.val + l2.val + carry) % 10
            newNode = ListNode(newVal)
            curNode.next = newNode
            curNode = newNode
            # next iteration
            carry = 1 if l1.val + l2.val >= 10 else 0
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            newVal = (l1.val + carry) % 10
            newNode = ListNode(newVal)
            curNode.next = newNode
            curNode = curNode.next
            carry = 1 if l1.val + carry >= 10 else 0
            l1 = l1.next
        
        while l2 is not None:
            newVal = (l2.val + carry) % 10
            newNode = ListNode(newVal)
            curNode.next = newNode
            curNode = newNode
            carry = 1 if l2.val + carry >= 10 else 0
            l2 = l2.next

        if carry:
            newNode = ListNode(1)
            curNode.next = newNode
            curNode = curNode.next

        return dummy.next
