import heapq


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        q = []
        adj = [[] for _ in range(n)]

        for u, v, d in edges:
            adj[u].append((d, v))

        heapq.heappush(q, (0, src))

        distances = {x: -1 for x in range(n)}

        while q:
            dst, cur = heapq.heappop(q)
            if distances[cur] != -1:
                continue
            distances[cur] = dst
            for d, neighbor in adj[cur]:
                if distances[neighbor] == -1: # not popped yet
                    packet = (dst + d, neighbor)
                    heapq.heappush(q, packet)

        return distances



        