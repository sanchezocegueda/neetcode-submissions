class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        prevMin = self.minStack[len(self.minStack)-1]
        if val < prevMin:
            self.minStack.append(val)
        else:
            self.minStack.append(prevMin)

    def pop(self) -> None:
        popped = self.stack.pop()
        _ = self.minStack.pop() # remove parallel minObj stack

        return popped

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack)-1]
        
