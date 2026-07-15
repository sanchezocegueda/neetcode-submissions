"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None:
            return

        stack = []

        marked = set()
        copy = {}

        stack.append(node)

        cp = Node(node.val)

        copy[node] = cp

        while stack:

            curr = stack.pop()

            if curr in marked:
                continue

            marked.add(curr)

            cp = copy[curr]

            for neighbor in curr.neighbors:
                if neighbor in copy:
                    neighbor_cp = copy[neighbor]
                else:
                    neighbor_cp = Node(neighbor.val, [])
                    copy[neighbor] = neighbor_cp

                cp.neighbors.append(neighbor_cp)
                stack.append(neighbor)
            
        return copy[node]

                

