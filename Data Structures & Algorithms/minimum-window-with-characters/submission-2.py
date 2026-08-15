

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
                
        l, r = 0, 0
        f = {}
        have = 0
        for c in t:
            if c not in f:
                f[c] = 1
            else:
                f[c] += 1

        need = len(f)

        best_len, best_str = math.inf, ""

        for r, c in enumerate(s):
            if c in f:
                f[c] -= 1

                if f[c] == 0:
                    have += 1
                
            while have == need:
                window_len = r - l + 1

                if window_len < best_len:
                    best_len = window_len
                    best_start = l
                
                left_char = s[l]
                if left_char in f:
                    f[left_char] += 1
                    
                    if f[left_char] > 0:
                        have -= 1
                
                l += 1

        if best_len == math.inf:
            return ""
        
        return s[best_start:best_start + best_len]

        return best_str