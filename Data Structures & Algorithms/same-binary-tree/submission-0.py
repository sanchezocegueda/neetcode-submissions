# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.p_stack = []
        self.q_stack = []

        def create_stack(t, is_p):
            
            if t is None:
                
                if is_p:
                    self.p_stack.append(t)
                else:
                    self.q_stack.append(t)

            else:
                if is_p:
                    self.p_stack.append(t.val)
                else:
                    self.q_stack.append(t.val)
                
                create_stack(t.left, is_p)
                create_stack(t.right, is_p)
        
        create_stack(p, True)
        create_stack(q, False)
    
        if len(self.p_stack) != len(self.q_stack):
            return False
        
        while len(self.p_stack) > 0:
            a, b = self.p_stack.pop(), self.q_stack.pop()
            if a != b:
                return False
            
        return True
                
