# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        prev = None
        curr = root

        while curr != None and curr.val != key:
            prev = curr
            if curr.val < key:
                curr = curr.right
            
            elif curr.val > key:
                curr = curr.left
        
        if curr != None: # there is something to remove
                

            left_child = curr.left
            right_child = curr.right

            if right_child != None: # promote
                new_child = right_child
                if left_child != None:
                    left_subtree = right_child
                    while left_subtree.left:
                        left_subtree = left_subtree.left
                    left_subtree.left = left_child
            elif left_child != None: # alternatively promote left
                new_child = left_child
            else: # leaf -- replace curr with None
                new_child = None
            
            if prev == None:
                return new_child
            elif curr.val < prev.val:
                # curr is left child
                prev.left = new_child


            else:
                # curr is right child
                prev.right = new_child
            
            
        return root
    