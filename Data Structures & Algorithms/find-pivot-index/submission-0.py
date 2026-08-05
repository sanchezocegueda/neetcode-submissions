class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sumLeft, sumRight = [0] * n, [0] * n
        l, r = 0, 0
        for i in range(n):
            sumLeft[i] = l
            sumRight[n-i-1] = r
            l += nums[i]
            r += nums[n-i-1]


        for i in range(n):
            if sumLeft[i] == sumRight[i]:
                return i
        
        return -1