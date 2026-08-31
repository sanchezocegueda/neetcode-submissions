class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        m = capacity
        n = len(profit)

        dp = [[-1] * (m+1) for _ in range(n)]



        m = capacity
        n = len(profit)

        dp = [[-1] * (m+1) for _ in range(n)]
        # dp[item][weight]

        # fill in 0-capacity column
        for i in range(n):
            dp[i][0] = 0
        
        # fill in first row (first item)
        for j in range(1, m+1):
            p = profit[0] if j >= weight[0] else 0
            dp[0][j] = p
        
        for i in range(1, n):
            for c in range(1, m+1):
                skip = dp[i-1][c] # skips item, same capacity
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[i-1][c-weight[i]]
                dp[i][c] = max(include, skip)
        
        return dp[n-1][m]
