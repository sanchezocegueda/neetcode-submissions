from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(l, r):
            rand = randint(l, r)
            nums[r], nums[rand] = nums[rand], nums[r]

            i = l
            pivot = r
            pivotNum = nums[r]

            for j in range(l, r):
                if nums[j] <= pivotNum: # swap and increment
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            nums[i], nums[pivot] = nums[pivot], nums[i]
            return i
        
        L, R = 0, len(nums)-1
        pivot = len(nums)

        # kth LARGEST, not kth smallest
        k = len(nums) - k

        while pivot != k:
            pivot = partition(L, R)

            if pivot < k: # search right partition
                L = pivot + 1
            
            else: # search left patition
                R = pivot - 1

        return nums[k]


