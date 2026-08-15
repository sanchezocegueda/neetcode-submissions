"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # easy solution: deep copy of regular linked list
        # add to stack
        # pop from stack and make the random pointers
        if head is None:
            return

        mirror = {}

        dummy = Node(0, head)
        dummyNew = Node(0)

        cur = head
        curNew = dummyNew

        while cur:
            newNode = Node(cur.val) # copy
            curNew.next = newNode
            curNew = newNode

            mirror[cur] = curNew
            cur = cur.next
        
        cur = head
        curNew = dummyNew.next
        while cur:
            curNew.random = mirror.get(cur.random)

            cur = cur.next
            curNew = curNew.next

        return dummyNew.next