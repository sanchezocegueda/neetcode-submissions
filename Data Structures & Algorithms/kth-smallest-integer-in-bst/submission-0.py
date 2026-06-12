# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        def dfs(t: Optional[TreeNode]):
            
            if t is None:
                return

            dfs(t.left)
            inorder.append(t.val)
            dfs(t.right)
            
        dfs(root)
        return inorder[k-1]