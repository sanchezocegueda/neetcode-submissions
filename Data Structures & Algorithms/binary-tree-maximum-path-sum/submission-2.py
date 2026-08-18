# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        self.maxVal = root.val
        def helper(node: Optional[TreeNode]) -> int:

            if not node:
                return 0
            
            left, right = helper(node.left), helper(node.right)

            split = node.val + left + right
            no_split = max(node.val + max(left, right), node.val)

            self.maxVal = max(self.maxVal, split, no_split)

            return no_split
        
        helper(root)

        return self.maxVal