class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l = 0
        r = n-1

        while True:
            dist = (r - l) // 2
            m = l + dist
            

            print(f"curr = {nums[m]}, m = {m}, l = {l}, r = {r}")

            if nums[m] < target:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
            
            if r < l:
                break
        
        return -1
        