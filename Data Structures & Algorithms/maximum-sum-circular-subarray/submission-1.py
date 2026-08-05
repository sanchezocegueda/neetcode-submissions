class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # idea: use kadane's, inf loop keeping track of pointers
        # stop when pointers overlap?
        if len(nums) == 0:
            return 0

        curMax, curMin = 0, 0
        globalMax, globalMin = nums[0], nums[0]
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            globalMax = max(globalMax, curMax)
            curMin = min(curMin + num, num)
            globalMin = min(globalMin, curMin)
            total += num

        return max(globalMax, total - globalMin) if globalMax >= 0 else globalMax