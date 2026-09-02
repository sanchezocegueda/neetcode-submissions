from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # shortest path ==> bfs

        # quick sanity check
        m, n = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[m-1][n-1] != 0:
            return -1

        q = deque()

        start = ((0, 0), 1) # ((i, j), d)

        marked = set()

        q.append(start)

        while q:

            src, d = q.popleft()

            if src == (m-1, n-1):
                return d # guaranteed to be optimal (bfs)

            if src in marked:
                continue
            
            marked.add(src)

            for a, b in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
                i, j = src
                r, c = i + a, j + b

                valid = 0 <= r < m and 0 <= c < n and grid[r][c] == 0
                if not valid or (r, c) in marked:
                    continue
                
                packet = ((r, c), d+1)
                
                q.append(packet)
        
        return -1
