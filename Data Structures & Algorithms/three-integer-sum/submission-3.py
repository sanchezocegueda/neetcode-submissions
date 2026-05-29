class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sort array
        nums.sort()
        n = len(nums)
        answers = []
        seen = set()
        
        # Run sorted 2-sum on remainder of array
        last = None
        for i in range(n):
            if last is not None and last == nums[i]:
                continue
            last = nums[i]
            l, r = i + 1, n-1
            target = -nums[i]

            while l < r:
                # Skip over the current number
                
                two_sum = nums[l] + nums[r]

                if two_sum < target:
                    l += 1
                elif two_sum > target:
                    r -= 1
                else:
                    answers.append([nums[i], nums[l], nums[r]])
                    
                    while l < n-1 and nums[l] == nums[l+1]:
                        l += 1
                    
                    while r > 1 and nums[r] == nums[r-1]:
                        r -= 1
                    
                    l += 1

        return answers
