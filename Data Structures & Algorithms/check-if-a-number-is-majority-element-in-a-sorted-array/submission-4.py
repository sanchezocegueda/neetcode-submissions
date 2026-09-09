class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # lower bound for both?
        
        def lower_bound(target, nums):

            l, r = 0, len(nums)

            while l < r:
                m = l + (r-l)//2

                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            
            return l
        
        n = len(nums)
        lower, upper = lower_bound(target, nums), lower_bound(target+1, nums)

        return lower < n and nums[lower] == target and upper-lower > n//2
            