class Solution:
    def solve(self, board: List[List[str]]) -> None:

        m, n = len(board), len(board[0])


        stack = []
        revert = []
        marked = set()
        for i in range(m):
            if board[i][0] == 'O':
                stack.append((i, 0))
            if board[i][n-1] == 'O':
                stack.append((i, n-1))

        for j in range(n):
            if board[0][j] == 'O':
                stack.append((0, j))
            if board[m-1][j] == 'O':
                stack.append((m-1, j))

        while stack:
            i, j = stack.pop()

            if (i, j) in marked:
                continue
            
            marked.add((i, j))
            
            for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                valid = 0 <= r < m and 0 <= c < n

                if valid and (r, c) not in marked and board[r][c] != 'X':
                    stack.append((r, c))

            board[i][j] = 'S'
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
        return


