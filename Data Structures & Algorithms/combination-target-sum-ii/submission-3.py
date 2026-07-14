class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        n = len(nums)

        self.combs = [] # avoid duplicates

        def helper(curNums, target, i, n):
            curSum = sum(curNums)

            if curSum == target:
                self.combs.append(curNums)
                return

            if curSum > target or i >= n:
                return
            
            
            w = helper(curNums + [nums[i]], target, i+1, n)

            curelt = nums[i]
            while i < n and curelt == nums[i]:
                i+=1
            wo = helper(curNums, target, i, n)

        helper([], target, 0, n)

        return self.combs