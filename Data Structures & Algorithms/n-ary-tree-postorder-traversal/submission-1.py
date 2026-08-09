"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = []
        postorder = []
        marked = set()
        stack.append(root)
        while stack:
            cur = stack.pop()

            if cur in marked:
                postorder.append(cur.val)
                continue
            
            marked.add(cur)

            stack.append(cur)
            for i in range(len(cur.children)-1, -1, -1):
                stack.append(cur.children[i])

        
        return postorder