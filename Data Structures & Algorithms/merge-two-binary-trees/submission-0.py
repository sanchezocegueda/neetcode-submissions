# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root1:
            return root2

        if not root2:
            return root1


        def dfs(node1, node2):
            
            if not node1 and not node2:
                return None

            newNode = TreeNode(0)



            newNode.val += node1.val if node1 is not None else 0
            newNode.val += node2.val if node2 is not None else 0

            l1 = node1.left if node1 is not None else None
            l2 = node2.left if node2 is not None else None
            r1 = node1.right if node1 is not None else None
            r2 = node2.right if node2 is not None else None

            leftNode = dfs(l1, l2)


            rightNode = dfs(r1, r2)
            
            newNode.left = leftNode
            newNode.right = rightNode


            return newNode

        newRoot = dfs(root1, root2)

        return newRoot
        