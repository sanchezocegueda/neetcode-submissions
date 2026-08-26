class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        f = Counter(nums)
        print(f)

        def helper(i, f, curPerm, perms):


            if i == len(nums):
                perms.append(curPerm)
                return
            
            for k in f.keys():
                if f[k] <= 0:
                    continue
                f[k] -= 1
                pCopy = curPerm.copy()
                pCopy.append(k)
                helper(i+1, f, pCopy, perms) # recurse
                f[k] += 1

        curPerm, perms = [], []
        helper(0, f, curPerm, perms)

        return perms
            

