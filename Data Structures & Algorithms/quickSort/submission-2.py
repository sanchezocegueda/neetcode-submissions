# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def helper(s, e):

            if e - s <= 1:
                return # already sorted
            
            i = s
            p = pairs[e-1].key # pivot (last elt in partition)
            for j in range(s, e):
                if pairs[j].key < p:
                    pairs[i], pairs[j] = pairs[j], pairs[i]
                    i += 1
            
            pairs[i], pairs[e-1] = pairs[e-1], pairs[i]

            helper(s, i)
            helper(i+1, e)

        n = len(pairs)
        helper(0, n) # [0, n) -- half-open interval

        return pairs # modifies in-place

