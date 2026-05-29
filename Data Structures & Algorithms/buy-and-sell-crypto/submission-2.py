class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)

        min_buy = prices[0]

        for i in range(1, n):
            profit = prices[i] - min_buy
            max_profit = max(profit, max_profit)
            min_buy = min(prices[i], min_buy)

        return max_profit