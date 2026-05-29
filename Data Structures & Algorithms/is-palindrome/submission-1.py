class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean up input string
        s = list(filter(str.isalnum, s.lower()))
        print(s)

        n = len(s)

        l = 0
        r = n - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True