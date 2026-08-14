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

        complements = set()

        def dfs1(node, complements):

            if node is None:
                return

            complements.add(target - node.val)

            dfs1(node.left, complements)
            dfs1(node.right, complements)
        
        dfs1(root1, complements)

        def dfs2(node, complements):
            if node is None:
                return False

            if node.val in complements:
                return True
            
            return dfs2(node.left, complements) or dfs2(node.right, complements)

        return dfs2(root2, complements)
            