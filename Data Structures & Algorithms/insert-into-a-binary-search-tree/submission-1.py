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
        
        newNode = TreeNode(val)

        # find appropriate place
        prev = None
        curr = root

        while curr != None:
            prev = curr
            if curr.val < val: # too small, search right
                curr = curr.right
            elif curr.val > val: # too big, search left
                curr = curr.left
            
        if prev.val < val:
            prev.right = newNode
        else:
            prev.left = newNode

        return root
