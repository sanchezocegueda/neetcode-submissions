class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board[0])

        # Check each row
        for i in range(n):
            seen = set()

            for j in range(n):
                char = board[i][j]
                if char != "." and char in seen:
                    return False
                else:
                    seen.add(char)

        # Check each col
        for i in range(n):
            seen = set()
            for j in range(n):
                char = board[j][i]
                if char != "." and char in seen:
                    return False
                else:
                    seen.add(char)

        # Check each box
        i = 0
        j = 0
        for i in range(0, n, 3):
            for j in range(0, n, 3):

                # new box
                seen = set()

                for k in range(i, i + 3):
                    for h in range(j, j + 3):
                        print(char)
                        char = board[k][h]
                        if char != "." and char in seen:
                            return False
                        else:
                            seen.add(char)
                
                

        
        return True # All tests passed, no tests failed

