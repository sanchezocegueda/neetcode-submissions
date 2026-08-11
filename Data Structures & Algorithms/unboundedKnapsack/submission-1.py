class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m, n = capacity, len(profit)
        
        # rows = capacity, cols = item
        dp = [[0] * (m+1) for _ in range(n)]

        # fill in first row
        for c in range(m+1):
            if weight[0] <= c: # enough capacity consumed
                dp[0][c] = (c // weight[0]) * profit[0]
    
        for i in range(1, n):
            for c in range(1, m+1):
                # skip
                skip = dp[i-1][c]

                # include
                incl = 0
                if c - weight[i] >= 0: # enough space in the knapsack
                    incl = profit[i] + dp[i][c-weight[i]]
                
                dp[i][c] = max(skip, incl)
        
        return dp[n-1][m]