class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while l < r:


            m = l + (r-l)//2

            if nums[m] == target:
                return m

            if nums[m] > nums[r]: # left sorted portion
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            
            else:
                if nums[m] < target <= nums[r]: # target is in the right
                    l = m+1
                else:
                    r = m-1

        

        return l if nums[l] == target else -1