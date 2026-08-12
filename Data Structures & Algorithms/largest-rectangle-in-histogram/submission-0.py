class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            
            if not stack or stack[-1][1] <= h: # stack is empty
                stack.append((i, h))


            else: # found a smaller rectangle
                cur_i = i
                while stack and stack[-1][1] > h:
                    prev_i, prev_h = stack.pop()
                    area = (i-prev_i) * prev_h
                    maxArea = max(area, maxArea)
                    cur_i, cur_h = prev_i, prev_h

                stack.append((cur_i, h))


        n = len(heights)

        while stack:
            start, height = stack.pop()
            maxArea = max(maxArea, height * (n - start))

        return maxArea