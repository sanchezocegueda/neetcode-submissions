class Solution:
    def hammingWeight(self, n: int) -> int:
        hw = 0
        for i in range(32):
            if 1 << i & n != 0:
                hw += 1
        
        return hw