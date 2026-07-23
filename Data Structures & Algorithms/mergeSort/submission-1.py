# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        n = len(pairs)

        if n == 0:
            return []

        if n == 1:
            return pairs # already sorted
        
        left = self.mergeSort(pairs[:n//2])
        right = self.mergeSort(pairs[n//2:])

        i, j = 0, 0

        res = []
        while True:
            if i >= n//2 and j >= (n - n//2): # done processing both
                break
            elif i < n//2 and  j >= (n-n//2): # done processing right
                res.append(left[i])
                i += 1
            elif i >= n//2 and j < (n - n//2): # done processing left
                res.append(right[j])
                j += 1 
            elif left[i].key <= right[j].key:
                res.append(left[i])
                i += 1
            elif left[i].key > right[j].key:
                res.append(right[j])
                j += 1
            
        
        return res


