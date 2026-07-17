class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur is not None and i < index:
            i += 1
            cur = cur.nxt
        
        if i == index and cur is not None:
            return cur.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        newHead = ListNode(val)
        newHead.nxt = self.head # works whether self.head is None or not
        self.head = newHead

        # empty list
        if self.tail is None:
            self.tail = newHead
        

    def insertTail(self, val: int) -> None:
        newTail = ListNode(val)
        if self.tail is not None:
            self.tail.nxt = newTail
        self.tail = newTail

        # empty list
        if self.head is None:
            self.head = newTail

    def remove(self, index: int) -> bool:
        prv = None
        cur = self.head
        i = 0

        while cur is not None and i < index:
            prv = cur
            cur = cur.nxt
            index -= 1
        
        if cur is None:
            return False

        if cur == self.head or cur == self.tail:
            if cur == self.head:
                self.head = cur.nxt
            
            if cur == self.tail:
                if prv is not None:
                    self.tail = prv
                    prv.nxt = None
            
        elif cur != self.head and cur != self.tail:
            prv.nxt = cur.nxt

        return True
        


    def getValues(self) -> List[int]:
        vals = []

        cur = self.head
        while cur is not None:
            vals.append(cur.val)
            cur = cur.nxt

        return vals