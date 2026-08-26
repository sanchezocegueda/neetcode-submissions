class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(i, nums):
            if i == len(nums):
                return [[]]
            
            resultPerms = []
            recursivePerms = helper(i+1, nums)
            for p in recursivePerms:
                # insert at each index
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    resultPerms.append(pCopy)
            return resultPerms
        
        return helper(0, nums)