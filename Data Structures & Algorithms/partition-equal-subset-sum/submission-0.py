class Solution:
    def canPartition(self, nums: List[int]) -> bool:
    
        numSum = sum(nums)

        if numSum % 2 == 1:
            return False
        
        target = numSum // 2
        n = len(nums)

        dp = set()
        dp.add(0)

        for i in range(n-1, -1, -1):
            nextDP = set()
            for t in dp:
                if nums[i] + t == target:
                    return True
                nextDP.add(nums[i] + t)
                nextDP.add(t)
            dp = nextDP
        
        return False