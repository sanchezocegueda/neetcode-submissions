

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
        while r < len(s):
            while have == need: # increase l
                if r-l < best_len:
                    best_len = r-l
                    best_str = s[l:r]
                
                c = s[l]
                if c in f: # do we even care about this character
                    f[c] += 1
                    if f[c] > 0:
                        have -= 1 # no longer meet criteria

                l += 1
            
            else: # increase r
                c = s[r]
                if c in f:
                    f[c] -= 1
                    if f[c] == 0:
                        have += 1
                
                r += 1
            
        while have == need: # increase l
            if r-l < best_len:
                best_len = r-l
                best_str = s[l:r]
            
            c = s[l]
            if c in f: # do we even care about this character
                f[c] += 1
                if f[c] > 0:
                    have -= 1 # no longer meet criteria

            l += 1

        return best_str