class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        max_run = 0

        while l < n:
            
            r = l
            seen = set()
            run = 0
            while r < n:
                if s[r] in seen:
                    l += 1
                    break
                
                seen.add(s[r])
                run += 1
                max_run = max(run, max_run)
                r += 1
            
            if not r < n:
                break
        
        return max_run