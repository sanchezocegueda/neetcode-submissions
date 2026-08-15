class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        maxima = []
        r = l = 0

        while r < len(nums):
            
            while q and nums[q[-1]] < nums[r]:
                q.pop() # pop smaller values from the right

            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                maxima.append(nums[q[0]])
                l += 1
            r += 1


        return maxima