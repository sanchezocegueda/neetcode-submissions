class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.cap = capacity
        self.size = 0

    def get(self, i: int) -> int:
        if 0 <= i and i < self.cap:
            return self.arr[i]
        else:
            return -1


    def set(self, i: int, n: int) -> None:
        if self.arr[i] is None:
            self.size += 1
        self.arr[i] = n
        
    def pushback(self, n: int) -> None:
        # resize array first if array is full
        if self.size == self.cap:
            self.resize()
        
        self.set(self.size, n)


    def popback(self) -> int:
        
        topop = self.arr[self.size-1]

        if topop is not None:
            self.size -= 1

        self.arr[self.cap-1] = None
        return topop
        

    def resize(self) -> None:
        extra = [None] * self.cap
        self.cap *= 2
        self.arr.extend(extra)

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap