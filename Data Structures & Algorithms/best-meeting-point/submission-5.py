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
            
        row_median = rows[len(rows) // 2]
        col_median = cols[len(cols) // 2]

        row_distance = 0
        for row in rows:
            row_distance += abs(row_median - row)
        
        col_distance = 0
        for col in cols:
            col_distance += abs(col_median - col)
        
        return row_distance + col_distance

        
