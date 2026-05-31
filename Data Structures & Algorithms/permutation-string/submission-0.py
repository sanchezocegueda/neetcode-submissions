from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        f = defaultdict(int)
        chars = set(s1)

        for c in s1:
            f[c] += 1

        l = 0
        rem = n1
        for r in range(n2):
            cr = s2[r]
            f[cr] -= 1
            if cr in chars and f[cr] >= 0:
                print(f"r: {r}, l: {l}, cr: {cr}, f[cr]: {f[cr]}, rem: {rem}")
                rem -= 1
            
            # Window at size
            if r - l + 1 > n1:
                cl = s2[l]
                f[cl] += 1 # leaving this one behind
                if cl in chars and f[cl] > 0:
                    rem += 1
                l += 1
            
            # new window at this point
            if rem == 0:
                return True
            
        return False

