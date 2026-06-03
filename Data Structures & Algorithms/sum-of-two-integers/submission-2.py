class Solution:
    def getSum(self, a: int, b: int) -> int:
        # use xor

        c = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            a_i = (a >> i) & 1
            b_i = (b >> i) & 1
            r_i = a_i ^ b_i ^ c
            c = (a_i & b_i | a_i & c | b_i & c)

            if r_i:
                res |= (1 << i)
            
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
            
        return res