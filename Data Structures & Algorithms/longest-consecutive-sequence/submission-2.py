class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        members = set(nums)

        top = 1
        run = 1
        seen = set()
        for num in nums:
        
            if num in seen:
                continue

            # Start a new run
            run = 1
            curr = num
            while (curr + 1) in members:
                run += 1
                top = max(top, run)
                seen.add(curr)
                curr += 1
            
        
        return top
