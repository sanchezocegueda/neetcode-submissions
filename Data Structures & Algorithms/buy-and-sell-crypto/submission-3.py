class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        min_buy = prices[0]

        for p in prices:
            cur = p - min_buy
            profit = max(cur, profit)
            min_buy = min(min_buy, p)




        return profit