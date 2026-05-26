class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        reciprocals = {}
        
        for i, num in enumerate(nums):

            rec = target - num

            other = reciprocals.get(rec)
            
            if other is not None:
                return [other, i]
            else:
                reciprocals[num] = i
            

        return [0, 0]