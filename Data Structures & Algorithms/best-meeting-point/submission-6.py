from collections import deque
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])


        rows, cols = [], [] # row positions and column positions of the friends

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: # found a friend
                    rows.append(i) # will be in order

        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    cols.append(j)

        distance = 0
        i, j = 0, len(rows)-1
        while i < j:
            distance += abs(rows[i] - rows[j])
            i += 1
            j -= 1

        i, j = 0, len(cols)-1
        while i < j:
            distance += abs(cols[i] - cols[j])
            i += 1
            j -= 1

        return distance

        
