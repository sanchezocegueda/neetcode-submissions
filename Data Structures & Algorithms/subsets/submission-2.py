class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets, curSet = [], []

        def helper(i, nums, curSet, subsets):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return
            
            # include
            curSet.append(nums[i])
            helper(i+1, nums, curSet, subsets)
            curSet.pop()

            # exclude
            helper(i+1, nums, curSet, subsets)
        
        helper(0, nums, curSet, subsets)
        return subsets