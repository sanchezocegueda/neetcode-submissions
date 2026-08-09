class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        for k in range(n): # row, col picker
            lenword = len(words[k])
            for i in range(lenword): # row counter
                if i >= n or k >= len(words[i]) or words[k][i] != words[i][k]:
                    return False

        return True
