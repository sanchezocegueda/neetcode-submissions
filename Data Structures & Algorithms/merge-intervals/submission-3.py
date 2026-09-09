class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        cur_interval = intervals[0]
        res.append(cur_interval)
        for l, r in intervals[1:]:
            if cur_interval[1] < l:
                cur_interval = [l, r]
                res.append(cur_interval)
            else:
                cur_interval[1] = max(r, cur_interval[1])
        return res