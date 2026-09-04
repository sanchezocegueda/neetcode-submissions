class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        i, n = 0, len(nums)
        reachable = [False] * n
        reachable[0] = True
        while i < n:
            if not reachable[i]:
                return False
            for j in range(i+1, i + nums[i]+1):
                if j >= n:
                    break
                reachable[j] = True
            i += 1
        
        return True