# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)

        if n <= 1:
            return pairs

        left = self.mergeSort(pairs[:n//2])
        right = self.mergeSort(pairs[n//2:])

        i, j = 0, 0

        res = []

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        while i < len(left):
            res.append(left[i])
            i += 1
        
        while j < len(right):
            res.append(right[j])
            j += 1

        return res



        


