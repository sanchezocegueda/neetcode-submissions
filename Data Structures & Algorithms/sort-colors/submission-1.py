
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = {0: 0, 1: 0, 2: 0}

        for num in nums:
            freq[num] += 1
        
        p = 0
        for i in range(3):
            while freq[i] > 0:
                nums[p] = i
                p += 1
                freq[i] -= 1
            
