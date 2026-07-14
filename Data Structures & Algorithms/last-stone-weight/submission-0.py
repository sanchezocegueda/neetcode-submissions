import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        elif len(stones) == 0:
            return 0
        
        # from now on, at least 2 stones are in the array

        maxHeap = [-s for s in stones] # turn min heap into max heap by negating numbers
        maxHeap.append(0)
        heapq.heapify(maxHeap)

        while True:
            bigger = -heapq.heappop(maxHeap)
            smaller = -heapq.heappop(maxHeap)

            if smaller == 0:
                return bigger

            new = 0
            if smaller < bigger:
                new = -(bigger - smaller)
            
            heapq.heappush(maxHeap, new)

        return 0