class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # Multi-source BFS from each house


        marked = {} # src |-> marked set
        num_houses = 0
        total_distance = {}
        times_marked = Counter()
        min_distance = math.inf
        m, n = len(grid), len(grid[0])

        q = deque() # for bfs

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    marked[(i, j)] = set()
                    num_houses += 1
                    q.append(((i, j), (i, j), 0)) # src, dst, d
                total_distance[(i, j)] = 0
            
        
        while q:
            src, dst, d = q.popleft()

            if dst in marked[src]:
                continue
            
            marked[src].add(dst)
            if src != dst:
                times_marked[dst] += 1
                total_distance[dst] += d
            
            if times_marked[dst] == num_houses: # found a meeting point for all houses
                min_distance = min(min_distance, total_distance[dst])
            
            i, j = dst
            for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                valid = 0 <= r < m and 0 <= c < n and grid[r][c] == 0
                if not valid or (r, c) in marked:
                    continue
                
                q.append((src, (r, c), d+1))
            



        return min_distance if min_distance < math.inf else -1


        