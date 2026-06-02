class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # create graph -- we want to run bfs with a queue

        m = len(grid)
        n = len(grid[0])

        adj = [[] for i in range(m * n)]
        queue = []
        num_fruit = 0
        # populate adjacency list
        for i in range(m):
            for j in range(n):
                # add neighbors to adj
                idx = i * n + j


                if i > 0 and grid[i-1][j] > 0: # up is defined
                    adj[idx].append((i-1, j))
                
                if i < m-1 and grid[i+1][j] > 0: # down is defined
                    adj[idx].append((i+1, j))

                if j > 0 and grid[i][j-1] > 0: # left is defined
                    adj[idx].append((i, j-1))
                
                if j < n-1 and grid[i][j+1] > 0: # right is defined
                    adj[idx].append((i, j+1))

                if grid[i][j] == 2: # fruit is initially rotten
                    package = ((i, j), 0)
                    queue.insert(0, package)

                if grid[i][j] > 0:
                    num_fruit += 1




        marked = set() # will add the marked fruits
        
        max_time = 0
        
        while len(queue) > 0:

            coord, timestamp = queue.pop()

            if coord in marked:
                continue # this fruit was processed before
            
            marked.add(coord)
            max_time = max(max_time, timestamp)
            
            i, j = coord
            idx = i * n + j

            for neighbor in adj[idx]:
                package = (neighbor, timestamp + 1)
                queue.insert(0, package)

        return max_time if len(marked) == num_fruit else -1