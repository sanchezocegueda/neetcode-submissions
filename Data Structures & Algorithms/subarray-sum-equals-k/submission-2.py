from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum
        # two pointers doesn't work bc it isn't monotonic
        n = len(nums)
        curSum = 0
        kCount = 0
        f = defaultdict(int)
        f[0] = 1
        for i in range(n):
            curSum += nums[i]
            kCount += f[curSum - k]
            f[curSum] += 1

            

        return kCount