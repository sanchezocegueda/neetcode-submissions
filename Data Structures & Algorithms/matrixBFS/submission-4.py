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
        grid[0][0] = 2
        

        while q:
            i, j, l = q.popleft()

            if i == m-1 and j == n-1:
                return l

            

            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                oob = i+a < 0 or i+a >= m or j+b < 0 or j+b >= n
                if not oob and grid[i+a][j+b] == 0:
                    grid[i+a][j+b] = 2
                    q.append((i+a, j+b, l+1))

        return -1
        