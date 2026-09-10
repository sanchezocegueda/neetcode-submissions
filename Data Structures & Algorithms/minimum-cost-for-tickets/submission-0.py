class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]
        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        daySet = set(days)
        for i in range(1, n+1):
            one_day = costs[0]
            seven_day = costs[1]
            thirty_day = costs[2]
            one_prev = dp[i-1]
            seven_prev = dp[i-7] if i - 7 >= 0 else 0
            thirty_prev = dp[i-30] if i - 30 >= 0 else 0


            if i in daySet:
                one = one_day + one_prev
                seven = seven_day + seven_prev
                thirty = thirty_day + thirty_prev
                dp[i] = min(one, seven, thirty)
            else:
                dp[i] = dp[i-1]
        print(dp)
        return dp[n]

