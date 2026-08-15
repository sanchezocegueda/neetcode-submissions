class Solution:
    def myPow(self, x: float, n: int) -> float:
        # double-and-add algorithm
        if n == 0:
            return 1
        negative = n < 0
        n = abs(n)
        result = 1.0
        current = x
        while n > 0:

            if n % 2 == 1:
                result *= current # multiply (add 1)
            current *= current # square (multiply exponent by 2)
            n //= 2
            

        return result if not negative else 1/result

