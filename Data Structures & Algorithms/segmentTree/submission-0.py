class Node:
    def __init__(self, total, L, R):
        self.sum = total
        self.L = L # left boundary
        self.R = R # right boundary
        self.left = None # left child
        self.right = None # right child

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self._build(nums, 0, len(nums)-1)

    def _build(self, nums, L, R):

        if L == R: # base case
            return Node(nums[L], L, R)

        root = Node(0, L, R)
        M = L + ((R - L) // 2)
        root.left = self._build(nums, L, M)
        root.right = self._build(nums, M+1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index: int, val: int) -> None:
        self._update_helper(self.root, index, val)

        
    
    def _update_helper(self, root, index, val):
        
        if root.L == root.R:
            root.sum = val
            return

        M = root.L + (root.R - root.L) // 2

        if index > M:
            self._update_helper(root.right, index, val) # only need to search right

        else:
            self._update_helper(root.left, index, val) # only need to search left

        root.sum = root.left.sum + root.right.sum
            


    def query(self, L: int, R: int) -> int:
        return self._query_helper(self.root, L, R)

    def _query_helper(self, root, L, R):

        if root.L > R or root.R < L: # are we oob?
            return 0
        
        if L <= root.L and root.R <= R: # is the whole subtree within the range?
            return root.sum
        
        return self._query_helper(root.left, L, R) + self._query_helper(root.right, L, R)



