class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # neetbot suggested better algorithm to what i wrote
        
        def lower_bound(value):
            # idea: find lower bound for the target
            #       and then find lower bound for target + 1
            lo, hi = 0, len(nums)

            while lo < hi:
                
                m = lo + (hi-lo) // 2

                if nums[m] < value:
                    lo = m+1
                else:
                    hi = m
            
            return lo

        start = lower_bound(target)

        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        
        end = lower_bound(target+1)-1

        return [start, end]