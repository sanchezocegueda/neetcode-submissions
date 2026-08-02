class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return n

        k = 0
        l = 0

        cur = nums[0]
        curCount = 0

        for r in range(n):
            if nums[r] == cur and curCount <= 1:
                curCount += 1
                nums[l] = nums[r]
                l += 1
                k += 1
            
            elif nums[r] > cur:
                curCount = 1
                cur = nums[r]
                nums[l] = nums[r]
                l += 1
                k += 1

        return k
                
