class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        minLength = math.inf

        l = -1
        curSum = 0
        for r in range(n):
            curSum += nums[r]
            while curSum >= target:
                minLength = min(minLength, r-l)
                l += 1
                curSum -= nums[l]


        return minLength if minLength < math.inf else 0