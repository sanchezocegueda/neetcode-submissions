class UnionFind:

    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.numComponents = n


    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.find(self.par[x])
            x = self.par[x]
        return x
    
    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
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

    def getNumComponents(self) -> int:
        return self.numComponents