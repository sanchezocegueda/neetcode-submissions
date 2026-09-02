class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        marked = {} # map of sets
        times_marked = {}
        total_distance = {}

        num_sources = 0
        min_distance = math.inf

        q = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                total_distance[(i, j)] = 0
                times_marked[(i, j)] = 0
                if grid[i][j] == 1:
                    marked[(i, j)] = set()
                    q.append(((i, j), (i, j), 0))
                    num_sources += 1

        while q:
            src, dst, d = q.popleft()


            if dst in marked[src]:
                continue
            marked[src].add(dst)
            if src != dst:
                total_distance[dst] += d
                times_marked[dst] += 1

            if times_marked[dst] == num_sources: # marked k times
                min_distance = min(min_distance, total_distance[dst])
                # print(dst, total_distance[dst], min_distance)


            # move on with the bfs
            i, j = dst
            for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                valid = 0 <= r < m and 0 <= c < n and grid[r][c] == 0
                # print(r, c, valid)
                if not valid or (r, c) in marked[src]:
                    continue
                packet = (src, (r, c), d+1)

                q.append(packet)

        return min_distance if min_distance < math.inf else -1


