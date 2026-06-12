# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # too greedy -- only takes parent into account
        def dfs(tree, l, r):

            if tree.left is None:
                left = True
            elif tree.left.val >= min(r, tree.val) or tree.left.val <= l:
                return False
            else:
                left = dfs(tree.left, l, min(r, tree.val))
            
            if tree.right is None:
                right = True
            elif tree.right.val <= max(l, tree.val) or tree.right.val >= r:
                return False
            else:
                right = dfs(tree.right, max(l, tree.val), r)

            
            return left and right


        return dfs(root, -math.inf, math.inf)