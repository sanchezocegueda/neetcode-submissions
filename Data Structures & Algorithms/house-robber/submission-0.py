from collections import defaultdict
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(int)

        for i in range(n):
            minus_one = dp[i-1]
            minus_two = dp[i-2]

            dp[i] = max(nums[i] + minus_two, minus_one)

        
        return dp[n-1]