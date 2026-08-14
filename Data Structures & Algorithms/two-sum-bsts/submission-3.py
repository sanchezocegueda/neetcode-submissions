# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        # use two-sum hash map approach
        # use bst property to avoid traversing the whole tree

        # no: use bst property to avoid using a hash map

        complements = set()


        def dfs(node):

            if node is None:
                return False
        
            if bst_search(root2, target-node.val):
                return True
            
            return dfs(node.left) or dfs(node.right)


        def bst_search(node, target):
            if node is None:
                return False
            
            if node.val == target:
                return True
            
            if target < node.val:
                return bst_search(node.left, target)
            else:
                return bst_search(node.right, target)

        return dfs(root1)
            