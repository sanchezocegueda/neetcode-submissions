class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def helper(i, curComb, combs, n, k):

            if len(curComb) == k: # found a subset of size k
                combs.append(curComb.copy())
                return
            if i > n: # no need to keep searching
                return

            for j in range(i, n+1):
                curComb.append(j)
                helper(j+1, curComb, combs, n, k)
                curComb.pop()
        
        combs, curComb = [], []
        helper(1, curComb, combs, n, k)
        return combs