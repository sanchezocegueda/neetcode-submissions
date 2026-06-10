# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        prev = None
        curr = root
        while curr != None:
            prev = curr
            if curr.val < val: # should go right
                curr = curr.right
            elif curr.val > val: # should go left
                curr = curr.left
        
        newNode = TreeNode(val)
        if prev.val < val:
            prev.right = newNode
        elif prev.val > val:
            prev.left = newNode

        return root