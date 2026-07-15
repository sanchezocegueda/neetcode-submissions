class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        marked = set()

        stack = []
        
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    stack.append((i, j, -1))

        num_islands = 0

        while stack:

            i, j, num = stack.pop()
            if (i, j) in marked:
                continue

            print(i, j, num)
            
            if num == -1:
                num_islands += 1 # new island
            
            # up
            if i > 0 and grid[i-1][j] == "1":
                stack.append((i-1, j, num_islands))

            # down
            if i < m-1 and grid[i+1][j] == "1":
                stack.append((i+1, j, num_islands))

            # left
            if j > 0 and grid[i][j-1] == "1":
                stack.append((i, j-1, num_islands))

            # right
            if j < n-1 and grid[i][j+1] == "1":
                stack.append((i, j+1, num_islands))

            marked.add((i, j))

        return num_islands