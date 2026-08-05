# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack = []

        stack.append(root)
        preorder = []

        while stack:
            cur = stack.pop()

            preorder.append(cur.val)
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is not None:
                stack.append(cur.left)

        return preorder