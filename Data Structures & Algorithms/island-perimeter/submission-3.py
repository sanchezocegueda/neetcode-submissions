class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        perimeter = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += 4

                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2

        return perimeter
        
        # dfs solution

        m, n = len(grid), len(grid[0])
        foundStart = False
        stack = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    foundStart = True
                    stack.append((i, j))
                    break
            
            if foundStart:
                break

        perimeter = 0
        marked = set()
        marked.add(stack[0])
        while stack:
            i, j = stack.pop()

            for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (i+r, j+c) in marked:
                    continue # is land and is marked

                validLand = i+r >= 0 and i+r < m and j+c >= 0 and j+c < n and grid[i+r][j+c] == 1

                if validLand:
                    marked.add((i+r, j+c))
                    stack.append((i+r, j+c))
                
                else:
                    perimeter += 1

        return perimeter
