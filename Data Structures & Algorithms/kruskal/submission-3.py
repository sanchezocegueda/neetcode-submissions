class UnionFind:

    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.n = n

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
        
        self.n -= 1
        return True
    
    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.find(self.par[x])
            x = self.par[x]
        
        return x

    def getNumComponents(self) -> int:
        return self.n

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:

        # idea: use unionfind data structure to keep track of ccs
        # sort edges by weight
        # add to mst as long as they do not create cycle

        uf = UnionFind(n)

        edges.sort(key=lambda e: e[2])

        mst_weight = 0

        for u, v, w in edges:
            if uf.union(u, v):
                mst_weight += w
            

        return mst_weight if uf.getNumComponents() == 1 else -1



