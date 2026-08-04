class NumArray:

    def __init__(self, nums: List[int]):

        n = len(nums)
        prefixSum = [0] * (n+1)

        for i in range(n):
            prefixSum[i] = prefixSum[((i-1) % n)] + nums[i]

        prefixSum.pop()

        self.prefixSum = prefixSum

        print(prefixSum)
    

    def sumRange(self, left: int, right: int) -> int:
        r = self.prefixSum[right]
        l = self.prefixSum[left-1] if left > 0 else 0
        return r - l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)