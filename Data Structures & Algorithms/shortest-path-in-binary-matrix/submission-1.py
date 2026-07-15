from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        q = deque()

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # at least there may be a valid path from now on

        mem = {}
        
        q.append((0, 0, 1))
        

        while q:

            i, j, d = q.popleft()

            if (i, j) in mem:
                continue
            
            mem[(i,j)] = d

            # up left
            if i > 0 and j > 0 and grid[i-1][j-1] == 0:
                q.append((i-1, j-1, d + 1))
            
            # up right
            if i > 0 and j < n-1 and grid[i-1][j+1] == 0:
                q.append((i-1, j+1, d + 1))

            # down right
            if i < n-1 and j < n-1 and grid[i+1][j+1] == 0:
                q.append((i+1, j+1, d + 1))
                
            # down left
            if i > 0 and j < n-1 and grid[i-1][j+1] == 0:
                q.append((i-1, j+1, d + 1))

            # up
            if i > 0 and grid[i-1][j] == 0:
                q.append((i-1, j, d + 1))

            # down
            if i < n-1 and grid[i+1][j] == 0:
                q.append((i+1, j, d + 1))

            
            # left
            if j > 0 and grid[i][j-1] == 0:
                q.append((i, j-1, d + 1))
            
            # right
            if j < n-1 and grid[i][j+1] == 0:
                q.append((i, j+1, d + 1))


        return mem[(n-1, n-1)] if (n-1, n-1) in mem else -1


