import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = [[] for _ in range(n+1)]

        for u, v, t in times:
            adj[u].append((t, v))
            # adj[v].append((t, u))
        
        q = [(0, k)]
        # heapq.heapify(q) NOT NEEDED (q is alr a valid heap)

        marked = [False] * (n+1)
        visited_count = 0

        while q:
            tu, u = heapq.heappop(q)

            if marked[u]:
                continue

            marked[u] = True
            visited_count += 1

            if visited_count == n:
                return tu

            for tv, v in adj[u]:
                if not marked[v]:
                    heapq.heappush(q, (tu + tv, v))
        
        return -1
            