
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        total_count = 0
        self.marked = set()
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j, m, n) -> int:
            if i < 0 or i >= m or j < 0 or j >= n: # out of bounds
                return 0
            elif (i, j) in self.marked: # invalid path
                return 0
            elif grid[i][j] == 1:
                return 0
            elif i == m-1 and j == n-1:
                return 1
            
            self.marked.add((i, j))

            left = dfs(i, j-1, m, n)
            right = dfs(i, j+1, m, n)
            up = dfs(i-1, j, m, n)
            down = dfs(i+1, j, m, n)

            self.marked.remove((i, j)) # allow for other paths

            return left + right + up + down

        return dfs(0, 0, m, n)

