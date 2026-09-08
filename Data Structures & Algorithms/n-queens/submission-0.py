class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # (r + c) is constant
        negDiag = set() # (r - c) is constant

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy) # always append copy
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue # will collide with other queens
                # update sets
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q"
                # recurse
                backtrack(r + 1)

                # cleanup for backtracking
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
            return
    
        backtrack(0)
        return res


