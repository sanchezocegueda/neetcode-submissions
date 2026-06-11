# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        levels = defaultdict(list)

        root_pack = (root, 0)
        q.append(root_pack)

        while len(q) > 0:
            curr, time_stamp = q.popleft()

            if curr is None:
                continue

            levels[time_stamp].append(curr.val)

            l_pack = (curr.left, time_stamp + 1)
            q.append(l_pack)
            r_pack = curr.right, time_stamp + 1
            q.append(r_pack)

        new_devils = []
        for level in levels.values():
            new_devils.append(level)
        return new_devils
            


            