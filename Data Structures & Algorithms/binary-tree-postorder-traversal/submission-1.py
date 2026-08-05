# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        marked = set()
        stack = []
        postorder = []
        stack.append(root)

        while stack:
            cur = stack.pop()
            if cur in marked:
                postorder.append(cur.val)
                continue

            marked.add(cur)
            stack.append(cur)

            if cur.right is not None:
                stack.append(cur.right)

            if cur.left is not None:
                stack.append(cur.left)
        
        return postorder