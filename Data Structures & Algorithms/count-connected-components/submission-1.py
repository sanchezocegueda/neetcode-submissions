class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs where you 

        unvisited = [i for i in range(n)]

        marked = set()

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        cc_count = 0

        while unvisited:
            root = unvisited.pop()

            if root in marked:
                continue
            
            cc_count += 1

            stack = [root]
            
            while stack:
                u = stack.pop()

                if u in marked:
                    continue
                
                marked.add(u)

                for v in adj[u]:
                    if v not in marked:
                        stack.append(v)
        
        return cc_count
