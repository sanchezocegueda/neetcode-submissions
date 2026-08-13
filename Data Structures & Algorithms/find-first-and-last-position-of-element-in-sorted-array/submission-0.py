class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        l, r = 0, len(nums)-1

        left_idx, right_idx = -1, -1

        def leftSearch(nums, l, r):
            if not nums or l > r:
                return -1

            m = l + (r-l) // 2

            if nums[m] < target: # search right half
                return leftSearch(nums, m+1, r)
            elif nums[m] > target: # search left half
                return leftSearch(nums, l, m-1) 
            else: # found one
                cand = leftSearch(nums, l, m-1)
                return cand if cand != -1 else m

        def rightSearch(nums, l, r):
            if not nums or l > r:
                return -1
            
            m = l + (r-l) // 2

            if nums[m] < target:
                return rightSearch(nums, m+1, r)
            elif nums[m] > target:
                return rightSearch(nums, l, m-1)
            else:
                cand = rightSearch(nums, m+1, r)
                return cand if cand != -1 else m



        return [leftSearch(nums, 0, len(nums)-1), rightSearch(nums, 0, len(nums)-1)]