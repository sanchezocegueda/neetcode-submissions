# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        stack = []
        s = 0

        stack.append(root)

        while stack:
            cur = stack.pop()

            if low <= cur.val <= high:
                s += cur.val
            
            if cur.right is not None:
                stack.append(cur.right)

            if cur.left is not None:
                stack.append(cur.left)

        
        return s