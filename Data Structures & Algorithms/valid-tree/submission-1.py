class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # preliminary condition
        if len(edges) != n-1:
            return False
        
        # check if connected
        stack = [0]

        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        marked = set()

        while stack:
            
            u = stack.pop()
            
            if u in marked:
                continue
            
            marked.add(u)

            for v in adj[u]:
                if v not in marked:
                    stack.append(v)

        return len(marked) == n