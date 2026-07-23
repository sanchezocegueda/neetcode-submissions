# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        # exclusive
        def helper(s, e):

            if e - s <= 1:
                return
            
            i = s
            p = pairs[e-1].key
            for j in range(s, e):
                if pairs[j].key < p:
                    pairs[i], pairs[j] = pairs[j], pairs[i]
                    i += 1
            
            # swap pivot
            pairs[i], pairs[e-1] = pairs[e-1], pairs[i]
        
            helper(s, i) # left
            helper(i+1, e) # right
        n = len(pairs)
        helper(0, n)

        return pairs

