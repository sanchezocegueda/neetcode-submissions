class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l, r = 0, 0

        while r < n:
            if nums[r] != val:
                nums[l] = nums[r] # move right non-val value to the left
                l += 1 # move left pointer for next non-val value

            r += 1
        
        return l # left pointer is at position k
