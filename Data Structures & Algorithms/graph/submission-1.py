class Graph:
    
    def __init__(self):
        self.adj = {}

    def addEdge(self, src: int, dst: int) -> None:
        # add to adjancency list

        if src not in self.adj:
            self.adj[src] = []
        
        if dst not in self.adj:
            self.adj[dst] = []

        if dst not in self.adj[src]:
            self.adj[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj or dst not in self.adj:
            return False

        if dst not in self.adj[src]:
            return False
        
        for i, x in enumerate(self.adj[src]):
            if x == dst:
                self.adj[src].pop(i)
                return True

        return False # should be unreachable

    def hasPath(self, src: int, dst: int) -> bool:
        # quick dfs
        
        marked = set()

        stack = [src]

        while stack:
            cur = stack.pop()
            
            if cur == dst:
                return True

            marked.add(cur)

            for neighbor in self.adj[cur]:
                if neighbor not in marked:
                    stack.append(neighbor)
                
        return False

