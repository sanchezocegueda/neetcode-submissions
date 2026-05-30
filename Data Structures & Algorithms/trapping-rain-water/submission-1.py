class Solution:
    def trap(self, height: List[int]) -> int:
        # Hint: use prefix and suffix sum
        n = len(height)
        if n <= 2:
            return 0

        # prefix computation
        prefix = [0 for i in range(n)]

        left_bar = 0
        for i in range(n):
            prefix[i] = max(0, left_bar - height[i])
            
            left_bar = max(left_bar, height[i])

        # suffix computation
        suffix = [0 for j in range(n)]

        right_bar = 0
        for j in range(n-1, -1, -1):
            suffix[j] = max(right_bar - height[j], 0)
            right_bar = max(right_bar, height[j])

        area = 0
        for k in range(n):
            area += min(prefix[k], suffix[k])

        return area
