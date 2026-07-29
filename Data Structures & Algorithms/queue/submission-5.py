class Node:
    def __init__(self, val, prv=None, nxt=None):
        self.value = val
        self.prv = prv
        self.nxt = nxt


class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        # add at tail
        new = Node(value)
        if self.size == 0: # self.head is None <=> self.tail is None
            self.head = new
            self.tail = new
            self.size += 1

        else:

            self.tail.nxt = new # add to the end of the queue
            new.prv = self.tail
            self.tail = new # change tail
            # head need not change
            self.size += 1
        

    def appendleft(self, value: int) -> None:
        # add at head

        new = Node(value)
        
        if self.size == 0: # self.tail is None <=> self.head is None
            self.head = new
            self.tail = new
            self.size += 1
        else:
            self.head.prv = new
            new.nxt = self.head
            self.head = new
            self.size += 1

    def pop(self) -> int:
        # pop at tail
        if self.size == 0:
            return -1


        elif self.size == 1:
            ret = self.tail.value
            self.head = None
            self.tail = None
            self.size = 0
            return ret

        else:
            ret = self.tail.value
            self.tail = self.tail.prv
            self.tail.nxt = None
            self.size -= 1
            return ret



    def popleft(self) -> int:
        # pop at head

        if self.size == 0:
            return -1
        
        elif self.size == 1:
            ret = self.head.value
            self.head = None
            self.tail = None
            self.size = 0
            return ret

        else:
            ret = self.head.value
            self.head = self.head.nxt
            self.head.prv = None
            self.size -= 1
            return ret