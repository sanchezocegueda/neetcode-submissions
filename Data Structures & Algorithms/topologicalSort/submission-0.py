
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
        
        marked = set()
        topoSort = []


        def dfs(u, path):

            if u in path: # cycle detected
                return False

            if u in marked: # node fully processed
                return True
            
            path.add(u)

            for v in adj[u]:
                if not dfs(v, path):
                    return False
            
            path.remove(u)
            marked.add(u)

            topoSort.append(u)
            return True
  
        for i in range(n):
            if i not in marked:
                if not dfs(i, set()):
                    return []
        
        topoSort.reverse()

        return topoSort