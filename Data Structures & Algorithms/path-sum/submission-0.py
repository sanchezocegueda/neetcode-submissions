# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def isLeaf(t: Optional[TreeNode]):
            return t.left is None and t.right is None
        

        def helper(t: Optional[TreeNode], targetSum: int):
            if t is None:
                return False
            
            if isLeaf(t) and targetSum - t.val == 0:
                return True

            return helper(t.left, targetSum - t.val) or helper(t.right, targetSum - t.val)
        
        return helper(root, targetSum)