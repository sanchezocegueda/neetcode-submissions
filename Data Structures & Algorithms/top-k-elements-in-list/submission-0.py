from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        n = len(nums)
        # pass 1: collect frequencies
        for num in nums:
            freqs[num] += 1
        

        # pass 2: add to buckets
        buckets = [[] for i in range(n)]
        all_nums = set(nums)
        print(freqs)
        for num in all_nums:
            idx = freqs[num] - 1
            buckets[idx].append(num)

        print(buckets)

        # pass 3: iterate through buckets in reverse
        i = n - 1
        answer = []
        while k > 0:
            if len(buckets[i]) > 0:
                answer.extend(buckets[i])
                k -= len(buckets[i])
            i -= 1

        return answer
        
        
        
        
        