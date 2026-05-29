class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [-1] * n
        suffix = [-1] * n

        prod = 1
        for i in range(n):
            prefix[i] = prod
            prod *= nums[i]
        
        prod = 1
        for j in range(n-1, -1, -1):
            suffix[j] = prod
            prod *= nums[j]

        answer = []
        for k in range(n):
            answer.append(prefix[k] * suffix[k])

        return answer
