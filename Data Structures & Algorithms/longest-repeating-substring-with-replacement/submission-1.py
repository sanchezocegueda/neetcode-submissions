from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f = defaultdict(int)
        l = 0
        max_freq = 0
        max_run = 0

        for r in range(len(s)):
            f[s[r]] += 1
            max_freq = max(max_freq, f[s[r]])

            # Window size minus the most frequent char = replacements needed
            while (r - l + 1) - max_freq > k:
                f[s[l]] -= 1
                l += 1
                # Note: we don't decrease max_freq here intentionally —
                # we only care about finding a *larger* valid window

            max_run = max(max_run, r - l + 1)

        return max_run