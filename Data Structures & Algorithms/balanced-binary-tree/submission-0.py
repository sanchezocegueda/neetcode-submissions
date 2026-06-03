# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def height(root):
            if root is None:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                self.balanced = False
            return max(left_height, right_height) + 1
        
        height(root)
        return self.balanced