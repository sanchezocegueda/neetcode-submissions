import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        if self.small and self.large and -self.small[0] >= self.large[0]:
            x = -heapq.heappop(self.small)
            heapq.heappush(self.large, x)

        if len(self.small) > len(self.large):
            x = -heapq.heappop(self.small)
            heapq.heappush(self.large, x)
    
        if len(self.large) > len(self.small):
            x = heapq.heappop(self.large)
            heapq.heappush(self.small, -x)


    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) < len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
        