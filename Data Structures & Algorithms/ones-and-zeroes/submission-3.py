class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # memoization version
        dp = {}

        def dfs(i, z, w):
            if i == len(strs):
                return 0
            if (i, z, w) in dp:
                return dp[(i, z, w)]
            
            skip = dfs(i + 1, z, w)
            include = 0
            if z - strs[i].count("0") >= 0 and w - strs[i].count("1") >= 0:
                include = dfs(i + 1, z-strs[i].count("0"), w-strs[i].count("1")) + 1 # include
            dp[(i, z, w)] = max(skip, include)
            return dp[(i, z, w)]


        return dfs(0, m, n)
