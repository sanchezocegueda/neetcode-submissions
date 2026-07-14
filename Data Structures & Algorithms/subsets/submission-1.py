class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.s = []
        n = len(nums)
        def dfs(curr_lst, i, n):
            if i == n:
                self.s.append(curr_lst)
                return
            
            dfs(curr_lst + [nums[i]], i+1, n)
            dfs(curr_lst, i+1, n)


        dfs([], 0, n)


        return self.s