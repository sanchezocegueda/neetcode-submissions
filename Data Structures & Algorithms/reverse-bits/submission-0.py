class Solution:
    def reverseBits(self, n: int) -> int:
        new = 0



        for i in range(32):
            new |= ((n >> i) & 1) << (31 - i)
        
        return new