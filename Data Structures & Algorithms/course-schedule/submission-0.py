from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        deg = [0] * numCourses
        q = deque()

        adj = [[] for _ in range(numCourses)]

        # build adjacency list
        for a, b in prerequisites:
            adj[a].append(b)

        # calculate indegrees
        for a in range(numCourses):
            for b in adj[a]:
                deg[b] += 1

        # add all vertices with indegree 0 to the queue
        for a in range(numCourses):
            if deg[a] == 0:
                q.append(a)

        # set visited count to 0
        visited = 0

        while q:
            a = q.popleft()
            visited += 1

            # reduce indegree of neighbors
            for b in adj[a]:
                deg[b] -= 1
                if deg[b] == 0:
                    q.append(b)
        
        return visited == numCourses