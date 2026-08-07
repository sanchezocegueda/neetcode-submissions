from enum import Enum

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        r = 1

        nums = arr

        n = len(arr)
        prev = nums[0]
        prevComp = "="
        maxLen = 1
        curLen = 1
        while r < n:
            cur = nums[r]

            if cur > prev:
                curComp = ">"
            elif cur < prev:
                curComp = "<"
            else:
                curComp = "="
            
            if curComp == "=":
                curLen = 1
            elif curComp == prevComp:
                curLen = 2
            else:
                curLen += 1
                maxLen = max(maxLen, curLen)

            r += 1
            prev = cur
            prevComp = curComp

        return maxLen