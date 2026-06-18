class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0

        min_len = min([len(s) for s in strs])

        disagree = False

        while i < min_len:
            c = strs[0][i]
            for s in strs[1:]:
                if s[i] != c:
                    disagree = True
                    break
            
            if disagree == True:
                break

            i += 1




        return strs[0][:i] if i > 0 else ""