# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        closest = root.val

        while root:
            lt = abs(target-root.val) < abs(target-closest)
            eq = abs(target-root.val) == abs(target-closest)

            if lt or (eq and root.val < closest):
                closest = root.val    

            if target < root.val:
                root = root.left
            else:
                root = root.right

        return closest
