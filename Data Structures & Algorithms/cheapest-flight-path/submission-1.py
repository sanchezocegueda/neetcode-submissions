import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        prices = [math.inf] * n

        prices[src] = 0


        for _ in range(k+1):
            next_prices = prices.copy()

            for u, v, cost in flights:
                if prices[u] == math.inf:
                    continue
                
                next_prices[v] = min(
                    next_prices[v],
                    prices[u] + cost
                )

            prices = next_prices

        return prices[dst] if prices[dst] < math.inf else -1