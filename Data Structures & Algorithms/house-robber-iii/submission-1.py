# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:


        def dfs(node):

            if not node:
                return (0, 0)
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                skip = max(left) + max(right) # (optionally) include both children, skip node
                incl = left[0] + right[0] + node.val # skip both children, include node
                

                return (skip, incl)

        return max(dfs(root))