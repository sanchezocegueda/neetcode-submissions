import heapq

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((w, v))
            adj[v].append((w, u))


        in_mst = [False] * n
        in_mst[0] = True
        mst_cost = 0
        mst_size = 1

        minHeap = [(w, v) for w, v in adj[0]]
        heapq.heapify(minHeap)

        while minHeap:
            w, v = heapq.heappop(minHeap)

            if in_mst[v]:
                continue
            
            if mst_size == n:
                break

            in_mst[v] = True
            mst_cost += w
            mst_size += 1

            for w2, neighbor in adj[v]:
                if not in_mst[neighbor]:
                    heapq.heappush(minHeap, (w2, neighbor))




        return mst_cost if mst_size == n else -1