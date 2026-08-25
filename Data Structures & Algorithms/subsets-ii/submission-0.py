class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        def helper(i, nums, curSet, subsets):

            if i >= len(nums):
                subsets.append(curSet.copy())
                return
            
            # include
            curSet.append(nums[i])
            helper(i+1, nums, curSet, subsets)
            curSet.pop()

            # exclude
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            helper(i+1, nums, curSet, subsets)

        nums.sort()

        subsets, curSet = [], []
        helper(0, nums, curSet, subsets)
        return subsets