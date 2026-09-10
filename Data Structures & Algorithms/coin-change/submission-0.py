class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [math.inf for i in range(amount+1)]
        dp[0] = 0

        for i in range(amount+1):
            res = math.inf
            for coin in coins:
                if i - coin >= 0 and dp[i-coin] < math.inf:
                    dp[i] = min(1 + dp[i-coin], dp[i])


        return dp[amount] if dp[amount] < math.inf else -1