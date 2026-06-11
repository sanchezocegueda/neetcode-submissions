# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()

        curr_level = 0
        
        if root != None:
            q.append(root)

        levels = []

        while len(q) > 0:
            level_len = len(q) # this loop only runs at each level
            level = []

            for i in range(level_len):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)
            
            levels.append(level)
            curr_level += 1

        return levels
            


            