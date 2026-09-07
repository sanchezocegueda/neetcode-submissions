class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not word:
            return False

        m, n = len(board), len(board[0])

        def dfs(i, j, word, marked):

            if not word or word[0] != board[i][j]:
                return False

            if word == board[i][j]:
                return True
            
            marked.add((i, j))

            for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                valid = 0 <= r < m and 0 <= c < n
                if not valid or (r, c) in marked:
                    continue
                res = dfs(r, c, word[1:], marked)
                if res:
                    return True
            marked.remove((i, j))
            return False
    
        for i in range(m):
            for j in range(n):
                marked = set()
                res = dfs(i, j, word, marked)
                if res:
                    return True
                    
        return False