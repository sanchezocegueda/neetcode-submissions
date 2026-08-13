from collections import deque
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rows, cols = [], []

        # find rows and columns of where the friends live        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)

        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    cols.append(j)
        

        row_median = rows[len(rows)//2]

        row_sum = sum(abs(pos - row_median) for pos in rows)
        
        col_median = cols[len(cols)//2]

        col_sum = sum(abs(pos - col_median) for pos in cols)

        return row_sum + col_sum
