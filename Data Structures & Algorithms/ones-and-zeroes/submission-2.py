class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = defaultdict(int)

        for s in strs:
            zCnt, wCnt = s.count("0"), s.count("1")
            for z in range(m, zCnt-1, -1):
                for w in range(n, wCnt-1, -1):
                    dp[(z, w)] = max(
                        1 + dp[(z - zCnt, w - wCnt)],
                        dp[(z, w)]
                    )
        
        return dp[(m, n)]
