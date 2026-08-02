class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # just count unique
        # AND modify nums

        n = len(nums)
        if n <= 1:
            return n

        l = 1

        k = 1

        cur = nums[0]

        for r in range(n):
            if nums[r] > cur:
                nums[l] = nums[r]
                cur = nums[r]
                k += 1
                l += 1


        return k