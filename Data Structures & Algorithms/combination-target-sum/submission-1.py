class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        self.sums = []

        def helper(curNums, target, i, n):
            curSum = sum(curNums)
            if curSum > target:
                return
            
            elif curSum == target:
                self.sums.append(curNums)
            
            for j in range(i, n):
                helper(curNums + [nums[j]], target, j, n)
        
        helper([], target, 0, n)
        return self.sums