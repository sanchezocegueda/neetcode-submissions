# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # enqueue right to left
        # only append first at any given level

        q = deque()

        q.append((root, 0))

        level = 0
        ret = []

        while q:
            tree, time = q.popleft()

            if tree is None:
                continue
            
            if level <= time:
                ret.append(tree.val)
                level += 1
            
            q.append((tree.right, time+1))
            q.append((tree.left, time+1))


        return ret