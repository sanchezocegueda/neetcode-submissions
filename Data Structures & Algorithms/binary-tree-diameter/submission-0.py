# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.d = 0

        
        self.height(root)

        return self.d

    
    def height(self, root):

        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        self.d = max(self.d, left_height + right_height)

        return max(left_height, right_height) + 1
        