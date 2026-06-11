# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        
        def dfs(t: Optional[TreeNode]):

            if t is None:
                return
            
            dfs(t.left)
            sol.append(t.val)
            dfs(t.right)

            return
        
        dfs(root)
        return sol