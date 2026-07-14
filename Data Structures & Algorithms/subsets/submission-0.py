class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.seen = set()

        def helper(nums: List[int]):

            if len(nums) == 0 or tuple(nums) in self.seen:
                return # subset already added

            else:
                self.seen.add(tuple(nums))

            # recurse with subsets
            for i in range(len(nums)):
                new = nums[:i]
                if i < len(nums)-1:
                    new.extend(nums[i+1:])
                
                print(new)

                helper(new)

        helper(nums)

        ret = [list(lst) for lst in self.seen]
        ret.append([])
        return ret