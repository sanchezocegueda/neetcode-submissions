class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0

        m = len(grid)
        n = len(grid[0])

        stack = []
        marked = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack.append((i, j, 1))


        def dfs(i, j) -> int:

            if (i, j) in marked:
                return 0
            
            marked.add((i, j))

            area = 1
            # up
            if i > 0 and grid[i-1][j] == 1:
                area += dfs(i-1, j)
            
            # down
            if i < m-1 and grid[i+1][j] == 1:
                area += dfs(i+1, j)

            # left
            if j > 0 and grid[i][j-1] == 1:
                area += dfs(i, j-1)

            # right
            if j < n-1 and grid[i][j+1] == 1:
                area += dfs(i, j+1)

            return area

        while stack:


            i, j, area = stack.pop()

            max_area = max(max_area, dfs(i, j))

        return max_area