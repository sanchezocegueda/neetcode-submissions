class Solution:
    def findMin(self, nums: List[int]) -> int:
        # at each step, look at neighbors
        l, r = 0, len(nums)-1

        while l < r:
            
            m = l + (r-l) // 2
            if nums[m] > nums[r]: # m is in left sorted portion; check right
                l = m + 1
            else: # m is in right sorted portion, check left
                r = m
        
        return nums[l]