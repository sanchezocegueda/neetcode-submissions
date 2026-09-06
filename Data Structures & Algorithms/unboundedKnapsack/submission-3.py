class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        m, n = capacity, len(profit)

        dp = [[0] * (m+1) for _ in range(n)]

        for c in range(m+1):
            if weight[0] <= c:
                dp[0][c] = (c // weight[0]) * profit[0]
        
        for i in range(1, n):
            for c in range(1, m+1):
                skip = dp[i-1][c]
                incl = 0

                if c - weight[i] >= 0:
                    incl = profit[i] + dp[i][c-weight[i]]
                
                dp[i][c] = max(skip, incl)


        return dp[n-1][m]

        ####


        m, n = capacity, len(profit)

        dp = [[0] * (m+1) for _ in range(n)]

        for c in range(m+1):
            if weight[0] <= c:
                dp[0][c] = (c // weight[0]) * profit[0] # however many we can grab
            
        
        for i in range(1, n):
            for c in range(1, m+1):
                skip = dp[i-1][c]


                incl = 0
                if c - weight[i] >= 0:
                    incl = profit[i] + dp[i][c-weight[i]]
                
                dp[i][c] = max(skip, incl)
        
        return dp[n-1][m]