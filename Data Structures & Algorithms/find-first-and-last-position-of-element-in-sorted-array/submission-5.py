class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # approach: find lower bound (first occurrence) of target and target + 1
        # say L is lower bound of target and R is lower bound of target + 1
        # then [L, R) is the desired range

        def lower_bound(target):
            l, r = 0, len(nums)

            while l < r:
                m = l + (r-l) // 2

                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l

        L, R = lower_bound(target), lower_bound(target+1)

        if L == len(nums) or R == 0 or nums[L] != target:
            return [-1, -1]
        
        return [L, R-1]
