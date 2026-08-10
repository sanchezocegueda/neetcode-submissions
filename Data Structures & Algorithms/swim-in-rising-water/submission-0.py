import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        

        n = len(grid)
        minHeap = [(grid[0][0], 0, 0)] # t, i, j

        marked = [[False] * n for _ in range(n)]



        while minHeap:
            t, i, j = heapq.heappop(minHeap)
            
            if i == n-1 and j == n-1:
                return t

            if marked[i][j]:
                continue

            marked[i][j] = True

            for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                valid = r >= 0 and r < n and c >= 0 and c < n

                if valid and not marked[r][c]:
                    newTime = max(t, grid[r][c])
                    heapq.heappush(minHeap, (newTime, r, c))
            

        return -1