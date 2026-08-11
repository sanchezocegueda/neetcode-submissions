import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        
        adj = {}

        for xi, yi in points:
            for xj, yj in points:
                if xi == xj and yi == yj:
                    continue
                

                if (xi, yi) not in adj:
                    adj[(xi, yi)] = []

                dst = abs(xi - xj) + abs(yi - yj)
                adj[(xi, yi)].append((dst, xj, yj))

                if (xj, yj) not in adj:
                    adj[(xj, yj)] = []
                adj[(xj, yj)].append((dst, xi, yi))

        n = len(adj)
        x0, y0 = points[0]
        minHeap = [(0, x0, y0)]
        mst = set()
        mst_components = 0
        mst_weight = 0

        while minHeap:
            dst, xi, yi = heapq.heappop(minHeap)

            if (xi, yi) in mst:
                continue
            
            mst.add((xi, yi))
            mst_components += 1
            mst_weight += dst
            
            if len(mst) == n:
                return mst_weight

            for dstj, xj, yj in adj[(xi, yi)]:
                if (xj, yj) not in mst:
                    heapq.heappush(minHeap, (dstj, xj, yj))


        return -1