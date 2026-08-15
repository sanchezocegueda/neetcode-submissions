class UnionFind:

    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.num_components = n

    def find(self, x: int) -> int:
        cur = x
        to_update = []
        while self.parent[cur] != cur:
            to_update.append(cur)
            cur = self.parent[cur]
        for u in to_update:
            self.parent[u] = cur # path compression
        return cur
    
    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y):
            return False
        xRoot = self.find(x)
        yRoot = self.find(y)
        self.parent[xRoot] = yRoot
        self.num_components -= 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # redundant edge is one that does not decrease number of ccs
        nodes = set()

        for u, v in edges:
            nodes.add(u)
            nodes.add(v)
        n = len(nodes) + 1
        uf = UnionFind(n)
        cand = None
        for u, v in edges:
            if not uf.union(u, v):
                cand = [u, v]

        return cand