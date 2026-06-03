class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        running_total = 0
        for i in range(n):
            running_total ^= nums[i]

        for j in range(n+1):
            running_total ^= j

        return running_total
