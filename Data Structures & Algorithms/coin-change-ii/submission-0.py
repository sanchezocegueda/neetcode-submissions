class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        m, n = len(coins), amount
        dp = [[0] * (n+1) for _ in range(len(coins))]

        for i in range(m):
            dp[i][0] = 1

        for i in range(m-1, -1, -1):
            for j in range(1, n+1):
                if j - coins[i] >= 0:
                    dp[i][j] += dp[i][j-coins[i]]
                if i+1 < m:
                    dp[i][j] += dp[i+1][j]
        # for row in dp:
        #     print(row)

        return dp[0][n]

