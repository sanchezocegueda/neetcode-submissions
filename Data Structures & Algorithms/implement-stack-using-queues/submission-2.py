from collections import deque
class MyStack:

    def __init__(self):
        self.size = 0
        self.q = None
        

    def push(self, x: int) -> None:
        
        new_q = deque()
        new_q.append(x)
        new_q.append(self.q)
        self.q = new_q
        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return -1
        
        ret = self.q.popleft()
        self.q = self.q.popleft()

        self.size -= 1
        return ret

    def top(self) -> int:
        if not self.empty():
            return self.q[0] # most recently added
        return -1

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()