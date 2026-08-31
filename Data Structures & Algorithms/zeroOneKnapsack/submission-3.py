class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        m = capacity
        n = len(profit)

        # dp[item][weight]
        dp = [[-1] * (m+1) for _ in range(n)]

        # fill in 0-cap column
        for i in range(n):
            dp[i][0] = 0

        # fill in first item row
        for c in range(1, m+1):
            dp[0][c] = profit[0] if c - weight[0] >= 0 else 0
        

        # do the rest
        for i in range(1, n):
            for c in range(1, m+1):
                skip = dp[i-1][c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[i-1][c-weight[i]]
                dp[i][c] = max(skip, include)
        
        return dp[n-1][m]
