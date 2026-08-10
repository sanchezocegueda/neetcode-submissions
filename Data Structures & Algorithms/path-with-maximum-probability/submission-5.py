import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]

        for i, (u, v) in enumerate(edges):
            sp = succProb[i]
            adj[u].append((v, sp))
            adj[v].append((u, sp))

        q = [(-1.0, start_node)]

        best = [0.0] * n
        best[start_node] = 1.0

        while q:

            spu, u = heapq.heappop(q)
            spu = -spu # make positive

            if spu < best[u]:
                continue

            if u == end_node:
                return spu

            # add all neighbors with the probability
            # note: must turn negative to maintain max heap
            for v, spv in adj[u]:
                new_prob = spu * spv
                # if v not in marked: replace
                if new_prob > best[v]:
                    best[v] = new_prob
                    heapq.heappush(q, (-new_prob, v))
        

        return 0



        