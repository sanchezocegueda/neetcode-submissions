import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = [[] for _ in range(n+1)]

        for u, v, t in times:
            adj[u].append((t, v))
            # adj[v].append((t, u))
        
        q = [(0, k)]
        heapq.heapify(q)

        minTime = 0
        marked = set()

        while q:
            tu, u = heapq.heappop(q)

            if u in marked:
                continue

            minTime = max(minTime, tu)

            marked.add(u)

            for tv, v in adj[u]:
                if v not in marked:
                    heapq.heappush(q, (tu + tv, v))
        
        return minTime if len(marked) == n else -1
            