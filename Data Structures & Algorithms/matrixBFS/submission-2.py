from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1 # no valid paths
        elif m == 1 and n == 1:
            return 0

        q = deque()
        q.append((0, 0, 0))
        

        while q:
            i, j, l = q.popleft()

            if i < 0 or i >= m or j < 0 or j >= n:
                continue

            if grid[i][j] != 0:
                continue

            if i == m-1 and j == n-1:
                return l

            grid[i][j] = 2

            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                q.append((i+a, j+b, l+1))

        return -1
        