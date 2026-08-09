# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        minDist = math.inf
        minCand = math.inf
        stack = [root]


        while stack:
            cur = stack.pop()
            
            if abs(target - cur.val) < minDist:
                minCand = cur.val
                minDist = abs(target-cur.val)
            
            elif abs(target-cur.val) == minDist:
                minCand = min(minCand, cur.val)

            if cur.right is not None:
                stack.append(cur.right)

            if cur.left is not None:
                stack.append(cur.left)


        return minCand
