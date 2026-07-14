import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-i for i in nums]
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)

        pushback = []
        for i in range(self.k):
            pushback.append(heapq.heappop(self.heap))
        ret = -pushback[-1]
        for num in pushback:
            heapq.heappush(self.heap, num)

        return ret

        
