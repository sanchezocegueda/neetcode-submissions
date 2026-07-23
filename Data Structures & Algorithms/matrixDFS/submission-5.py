
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return 0

        def dfs(i, j) -> int:

            if i < 0 or i >= m or j < 0 or j >= n: # out of bounds
                return 0
            elif grid[i][j] != 0: # invalid path
                return 0
            elif i == m-1 and j == n-1:
                return 1
            
            grid[i][j] = 2 # mark as visited
            
            count = 0
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                count += dfs(i + a, j + b)

            grid[i][j] = 0

            return count

        return dfs(0, 0)

