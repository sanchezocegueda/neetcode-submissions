# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        self.good = 0
        def dfs(t, curMax):
            if t is None:
                return
            
            if t.val >= curMax:
                curMax = t.val
                self.good += 1
            
            dfs(t.left, curMax)
            dfs(t.right, curMax)

        
        dfs(root, -1000)

        return self.good