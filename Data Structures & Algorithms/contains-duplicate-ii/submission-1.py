from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = defaultdict(int)
        n = len(nums)

        if n <= 1:
            return False
        
        # assert k <= n

        l = 0
        r = 0

        while r <= k:

            freq[nums[r]] += 1
            if freq[nums[r]] > 1:
                return True
            r += 1
        

        while r < n:
            freq[nums[l]] -= 1
            l += 1

            freq[nums[r]] += 1
            if freq[nums[r]] > 1:
                return True
            r += 1            

        return False
        
        
