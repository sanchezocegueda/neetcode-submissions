class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # brute force solution


        n = len(nums)
        dp = Counter() # cache the sums?
        dp[0] = 1

        for i in range(n):
            newDP = Counter()
            for s in dp.keys():
                plus = s + nums[i]
                minus = s - nums[i]
                
                newDP[plus] += dp[s]
                newDP[minus] += dp[s]
            dp = newDP

        # dp[0] -= 1 # remove the initial one

        return dp[target]
        