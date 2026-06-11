# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # could use a queue for level search
        memo_p = set()
        memo_q = set()
        lowestAncestor = root

        def isAncestor(t: TreeNode, v: int, mem: set):
            if t is None:
                return False
            if t.val == v or t.val in mem:
                mem.add(t.val)
                return True
            
            elif t.val < v: # too small, look right
                ans = isAncestor(t.right, v, mem)
                if ans == True:
                    mem.add(t.val)
                return ans
            
            elif t.val > v:
                ans = isAncestor(t.left, v, mem)
                if ans == True:
                    mem.add(t.val)
                return isAncestor(t.left, v, mem)

        isAncestor(root, p.val, memo_p)
        isAncestor(root, q.val, memo_q)

        queue = deque()

        queue.append(root)
        while len(queue) > 0:
            curr = queue.popleft()
            lowestAncestor = curr
            if curr.left != None and isAncestor(curr.left, p.val, memo_p) and isAncestor(curr.left, q.val, memo_q):
                queue.append(curr.left)

            if curr.right != None and isAncestor(curr.right, p.val, memo_p) and isAncestor(curr.right, q.val, memo_q):
                queue.append(curr.right)

        return lowestAncestor