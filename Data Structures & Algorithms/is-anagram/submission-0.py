from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count_s = defaultdict(int)
        count_t = defaultdict(int)
        all_letters = set()

        for c in s:
            count_s[c] += 1
            all_letters.add(c)
        
        for c in t:
            count_t[c] += 1
            all_letters.add(c)

        for l in all_letters:
            if count_s[l] != count_t[l]:
                return False
            
        return True
        
        