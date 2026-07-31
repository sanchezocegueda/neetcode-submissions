class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # this is a reachability problem
        # build a graph, then dfs to check for reachability
        # connected components?
        # easier question: which nodes are reachable from atlantic
        # then which nodes are reachable from pacific?

        m, n = len(heights), len(heights[0])

        # part 1: pacific
        # init: first column, first row
        stack = []

        for i in range(m):
            stack.append((i, 0, heights[i][0]))

        for j in range(n):
            stack.append((0, j, heights[0][j]))
        

        pMarked = set()
        
        while stack:

            i, j, h = stack.pop()

            if (i, j) in pMarked:
                continue
            
            pMarked.add((i, j))

            for r, c in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                oob = i+r < 0 or i+r >= m or j+c < 0 or j+c >= n and (i+r, j+c)
                valid = not oob and (i+r, j+c) not in pMarked
                if valid and heights[i+r][j+c] >= heights[i][j]:
                    stack.append((i+r, j+c, heights[i+r][j+c]))
                

        # part 2: atlantic
        # init: last column, last row
        aMarked = set()
        

        for i in range(m):
            stack.append((i, n-1, heights[i][n-1]))

        for j in range(n):
            stack.append((m-1, j, heights[m-1][j]))
        


        while stack:

            i, j, h = stack.pop()

            if (i, j) in aMarked:
                continue
            
            aMarked.add((i, j))

            for r, c in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                oob = i+r < 0 or i+r >= m or j+c < 0 or j+c >= n and (i+r, j+c)
                valid = not oob and (i+r, j+c) not in aMarked
                if valid and heights[i+r][j+c] >= heights[i][j]:
                    stack.append((i+r, j+c, heights[i+r][j+c]))
                

        res = []

        for i in range(m):
            for j in range(n):
                if (i,j) in aMarked and (i,j) in pMarked:
                    res.append([i, j])
    
        return res