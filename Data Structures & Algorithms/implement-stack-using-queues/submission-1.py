from collections import deque
class MyStack:

    def __init__(self):
        self.size = 0
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return -1
        
        for i in range(self.size - 1):
            self.q.append(self.q.popleft())
        self.size -= 1
        return self.q.popleft()

    def top(self) -> int:
        if not self.empty():
            return self.q[self.size-1] # most recently added
        return -1

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()