# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        dummy = TreeNode(-1)
        seenp, seeni = set(), set()
        n = len(preorder)
        p, i = 0, 0

        preorder, inorder = deque(preorder), deque(inorder)
        nodes = {}

        # for i in inorder:
        #     node = TreeNode(i)
        #     nodes[i] = node
        
        prevNum = "a"
        nodes["a"] = dummy
        prevNode = dummy

        while preorder:
        # while p < n:
            curNum = preorder.popleft()
            curNode = TreeNode(curNum)
            nodes[curNum] = curNode
            
            seenp.add(curNum)

            if prevNum in seeni:
                prevNode.right = curNode

            else:
                prevNode.left = curNode


            # process these?
            while inorder and inorder[0] in seenp:
                curNum = inorder.popleft()
                seeni.add(curNum)

            prevNum = curNum
            prevNode = nodes[prevNum]

        return dummy.left
