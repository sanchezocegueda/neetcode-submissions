class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n, total = len(stones), sum(stones)
        
        dp = set([total])

        minSum = total
        for x in stones:
            newDP = set()
            for t in dp:
                newDP.add(t)
                newSum = t - (2*x)
                if newSum >= 0:
                    newDP.add(newSum)
                    minSum = min(minSum, newSum)
            dp = newDP
        return minSum
                


