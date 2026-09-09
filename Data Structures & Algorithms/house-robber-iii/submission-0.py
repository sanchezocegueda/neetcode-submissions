# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        dp = {}

        def dfs(node):

            if node in dp:
                return dp[node]

            if not node:
                dp[node] = (0, 0) # skip, include
                return 0
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                skip = max(dp[node.left]) + max(dp[node.right]) # (optionally) include both children, skip node
                incl = dp[node.left][0] + dp[node.right][0] + node.val # skip both children, include node
                
                dp[node] = (skip, incl)


        dfs(root)

        return max(dp[root])