class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        # Already connected
        if root_x == root_y:
            return False

        # Swap if root_x < root_y
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        
        return True


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        new_edges = sorted(edges, key=lambda x: x[2])

        mst = UnionFind(n)
        edges_used = 0
        mst_weight = 0

        for u, v, w in new_edges:

            if mst.find(u) == mst.find(v):
                continue # would create a cycle

            mst.union(u, v) 

            edges_used += 1
            mst_weight += w
            if edges_used == n-1:
                return mst_weight



        return -1