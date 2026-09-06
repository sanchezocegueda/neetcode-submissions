import heapq


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        
        q = [(0, src)]

        marked = set()

        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        distances = {u:-1 for u in range(n)}

        while q:
            d, u = heapq.heappop(q)

            if u in marked:
                continue

            marked.add(u)

            distances[u] = d

            for v, w in adj[u]:
                if v in marked:
                    continue
                packet = (w + d, v)
                heapq.heappush(q, packet)


            
        
        return distances



        