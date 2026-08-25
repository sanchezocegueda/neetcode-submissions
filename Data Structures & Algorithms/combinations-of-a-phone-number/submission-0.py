class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n, k = len(digits), len(digits)
        if n == 0:
            return []
        
        digit_letters = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        
        def helper(i, curComb, combs, n, k):
            if len(curComb) == k:
                combs.append("".join(curComb))
                return

            if i > n:
                return
            
            for letter in digit_letters[digits[i]]:
                curComb.append(letter)
                helper(i+1, curComb, combs, n, k)
                curComb.pop()

        curComb, combs = [], []
        helper(0, curComb, combs, n, k)
        return combs