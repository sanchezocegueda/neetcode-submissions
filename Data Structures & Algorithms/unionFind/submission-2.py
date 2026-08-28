class UnionFind:
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.num_components = n
    

    def union(self, x: int, y: int) -> bool:
        """Put x and y into the same component"""
        xRoot, yRoot = self.find(x), self.find(y)
        if xRoot == yRoot:
            return False # don't need to do anything


        if self.rank[xRoot] <= self.rank[yRoot]:
            self.par[xRoot] = yRoot
            self.rank[yRoot] += self.rank[xRoot]
        else:
            self.par[yRoot] = self.par[xRoot]
            self.rank[xRoot] = self.rank[yRoot]

        self.num_components -= 1

        return True


    def find(self, x: int) -> int:
        """Return x's root"""
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        
        return x
    
    def isSameComponent(self, x: int, y: int) -> bool:
        """Determines whether x and y are in the same component"""
        return self.find(x) == self.find(y)
    
    def getNumComponents(self) -> int:
        return self.num_components