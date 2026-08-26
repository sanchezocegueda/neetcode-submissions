class UnionFind:

    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x: int, y: int) -> False:
        xRoot, yRoot = self.find(x), self.find(y)
        
        if xRoot == yRoot:
            return False
        
        if self.rank[xRoot] >= self.rank[yRoot]:
            self.par[yRoot] = xRoot
            self.rank[xRoot] += self.rank[yRoot]
        else:
            self.par[xRoot] = yRoot
            self.rank[yRoot] += self.rank[xRoot]
        
        return True
        


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        for i, e in enumerate(edges):
            e.append(i)
        
        edges.sort(key=lambda e: e[2])

        mst_weight = 0

        uf = UnionFind(n)
        
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w
        
        critical, pseudo = [], []

        for n1, n2, edge_weight, i in edges:
            # skip current edge
            weight = 0
            uf = UnionFind(n)
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    weight += w
            if max(uf.rank) < n or weight > mst_weight:
                critical.append(i)
                continue
            
            # Try with current edge
            uf = UnionFind(n)
            weight = edge_weight
            uf.union(n1, n2)
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weight += w
            
            if weight == mst_weight:
                pseudo.append(i)
        
        return [critical, pseudo]







