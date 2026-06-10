class Solution:
    dp = {-1: 0, 0: 1, 1: 1}
    seen = {0, 1}
    def climbStairs(self, n: int) -> int:
        if n in self.seen:
            return self.dp[n]

        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.seen.add(n)
        self.dp[n] = res

        return res