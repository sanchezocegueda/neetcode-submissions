class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            minus_one, minus_two = 0, 0

            for num in nums:
                curr = max(minus_one, minus_two + num)
                minus_two = minus_one
                minus_one = curr
            
            return curr

        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        
        return max(helper(nums[:n-1]), helper(nums[1:]))