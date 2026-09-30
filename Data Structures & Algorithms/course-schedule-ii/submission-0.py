class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # toposort!

        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)

        
        marked = set()

        def dfs(u, path):

            if u in path:
                return False

            if u in marked:
                return True
            
            path.add(u)

            for v in adj[u]:
                if not dfs(v, path):
                    return False
            
            marked.add(u)
            path.remove(u)
            topoSort.append(u)
            return True

        topoSort = []
        for i in range(numCourses):
            if not dfs(i, set()):
                return []
        

        return topoSort
        