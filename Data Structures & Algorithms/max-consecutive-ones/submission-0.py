class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0

        ones = False
        run = 0
        for num in nums:
            if num == 1:
                ones = True
            else:
                ones = False
                run = 0
            if ones:
                run += 1
                maxOnes = max(maxOnes, run)

        return maxOnes
            
                