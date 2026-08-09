class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            
            s = 0
            while n > 0:
                digit = n % 10
                n //= 10
                s += digit**2

            if s in seen:
                return False
            seen.add(s)
            n = s
        return True