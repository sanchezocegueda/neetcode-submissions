class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.num_components = n

    def find(self, x: int) -> int:
        cur = x
        to_update = []
        while self.parent[cur] != cur: # get to the top of the find
            to_update.append(cur)
            cur = self.parent[cur]
        for u in to_update:
            self.parent[u] = cur

        return cur

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x,y):
            return False
        xRoot = self.find(x)
        yRoot = self.find(y)
        self.parent[xRoot] = yRoot
        self.num_components -= 1
        return True


    def getNumComponents(self) -> int:
        return self.num_components
