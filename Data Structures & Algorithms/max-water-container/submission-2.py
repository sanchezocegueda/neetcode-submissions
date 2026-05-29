class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1

        max_area = 0
        while r > l:
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, area)
        
            # Strict improvement
            if heights[l] < heights[r]:
                l += 1

            # Strict improvement?
            else:
                r -= 1
        

        return max_area
