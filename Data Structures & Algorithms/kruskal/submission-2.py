class UnionFind:

    def __init__(self, n: int):
        self.numComponents = n
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def union(self, x: int, y: int) -> bool:
        xRoot, yRoot = self.find(x), self.find(y)

        if xRoot == yRoot:
            return False
        
        if self.rank[xRoot] <= self.rank[yRoot]:
            self.par[xRoot] = yRoot
            self.rank[yRoot] += self.rank[xRoot]
        else:
            self.par[yRoot] = xRoot
            self.rank[xRoot] += self.rank[yRoot]
        
        self.numComponents -= 1
        return True

    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.find(self.par[x]) # path compression
            x = self.par[x]
        return x

    def getNumComponents(self):
        return self.numComponents


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # sort edges by weight and add them to mst 

        edges.sort(key = lambda e: e[2])

        mst_weight = 0
        uf = UnionFind(n)

        for u, v, w in edges:

            if uf.union(u, v): # not in same component before
                mst_weight += w

        return mst_weight if uf.getNumComponents() == 1 else -1

