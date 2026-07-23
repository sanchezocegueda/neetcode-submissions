
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        self.marked = set()
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j) -> int:
            if i < 0 or i >= m or j < 0 or j >= n: # out of bounds
                return 0
            elif (i, j) in self.marked: # invalid path
                return 0
            elif grid[i][j] == 1:
                return 0
            elif i == m-1 and j == n-1:
                return 1
            
            self.marked.add((i, j))

            left = dfs(i, j-1)
            right = dfs(i, j+1)
            up = dfs(i-1, j)
            down = dfs(i+1, j)

            self.marked.remove((i, j)) # allow for other paths

            return left + right + up + down

        return dfs(0, 0)

