class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # multi-source bfs
        # graph nodes are treasure and land cells
        # sources are treasure chests

        m = len(grid)
        n = len(grid[0])
        adj = [[] for i in range(m * n)]
        INF = (1 << 31) - 1

        queue = []

        for i in range(m):
            for j in range(n):

                if grid[i][j] == -1: # do not want this in the graph
                    continue

                idx = i * n + j

                if i > 0 and grid[i-1][j] != -1: # up
                    adj[idx].append((i-1, j))
                
                if i < m-1 and grid[i+1][j] != -1: # down
                    adj[idx].append((i+1, j))

                if j > 0 and grid[i][j-1] != -1: # left
                    adj[idx].append((i, j-1))
                
                if j < n-1 and grid[i][j+1] != -1: # right
                    adj[idx].append((i, j+1))
                
                if grid[i][j] == 0:
                    package = ((i, j), 0)
                    queue.insert(0, package)


        marked = set()

        while len(queue) > 0:
            coord, timestamp = queue.pop()

            if coord in marked:
                continue

            marked.add(coord)

            i, j = coord

            grid[i][j] = timestamp

            idx = i * n + j
            for neighbor in adj[idx]:
                print(neighbor, timestamp+1)
                package = (neighbor, timestamp+1)
                queue.insert(0, package)



        return