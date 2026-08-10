import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]

        for i in range(len(edges)):
            u, v = edges[i]
            sp = succProb[i]
            adj[u].append((v, sp))
            adj[v].append((u, sp))

        print(adj)

        q = [(-1, start_node)]

        heapq.heapify(q)
        marked = set()

        while q:

            spu, u = heapq.heappop(q)

            spu = -spu # make positive

            if u == end_node:
                return spu

            elif u in marked:
                continue
            
            marked.add(u)

            # add all neighbors with the probability
            # note: must turn negative to maintain max heap
            for v, spv in adj[u]:

                if v not in marked:
                    heapq.heappush(q, (-spu * spv, v))
        

        return 0



        