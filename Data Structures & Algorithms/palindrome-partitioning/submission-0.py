class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        def isPalindrome(s: str):
            # meta way
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True


        palindromes = []
        part = []

        def dfs(i):
            if i >= len(s):
                palindromes.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)

        return palindromes