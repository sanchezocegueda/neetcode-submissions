class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        if len(nums) == 0:
            return 0
        
        curSum = 0
        maxSum = nums[0]

        for num in nums:
            curSum = max(curSum + num, num) # continue subarray or start fresh
            maxSum = max(maxSum, curSum)
        
        return maxSum