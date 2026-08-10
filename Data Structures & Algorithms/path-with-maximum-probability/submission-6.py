import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]

        for (u, v), prob in zip(edges, succProb):
            adj[u].append((v, prob))
            adj[v].append((u, prob))

        q = [(-1.0, start_node)]

        best = [0.0] * n
        best[start_node] = 1.0

        while q:

            uProb, u = heapq.heappop(q)
            uProb = -uProb # make positive

            if u == end_node:
                return uProb

            if uProb < best[u]:
                continue


            # add all neighbors with the probability
            # note: must turn negative to maintain max heap
            for v, vProb in adj[u]:
                new_prob = uProb * vProb
                if new_prob > best[v]:
                    best[v] = new_prob
                    heapq.heappush(q, (-new_prob, v))
        

        return 0



        