# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        states = []

        states.append([pair for pair in pairs])

        
        for i in range(1, len(pairs)):
            p = pairs[i]
            j = i - 1

            while j >= 0 and p.key < pairs[j].key:
                pairs[j+1] = pairs[j]
                j -= 1
            pairs[j+1] = p
            states.append([pair for pair in pairs])
        
        return states


