from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        k = len(nums) - k
        def quickSelect(l, r):
            # randomize pivot selection by making rightmost element a random choice in the array
            rand = randint(l, r)
            nums[rand], nums[r] = nums[r], nums[rand]

            i = l
            pivot = nums[r]

            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            nums[i], nums[r] = nums[r], nums[i] # final swap

            if i < k: # search right
                return quickSelect(i+1, r)
            elif i > k: # search left
                return quickSelect(l, i-1)
            else: # found it
                return nums[i]

        return quickSelect(0, n-1)


