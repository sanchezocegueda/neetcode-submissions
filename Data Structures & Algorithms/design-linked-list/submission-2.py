class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.nxt = None
        self.prv = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if self.size == 0 or index < 0 or index > self.size-1:
            return -1

        cur = self.head
        while index > 0:
            cur = cur.nxt
            index -= 1
        
        return cur.val

    def addAtHead(self, val: int) -> None:
        newHead = ListNode(val)
        
        newHead.nxt = self.head

        if self.size == 0:
            self.tail = newHead # no previous head
        else:
            self.head.prv = newHead
        
        self.head = newHead

        self.size += 1
        return

    def addAtTail(self, val: int) -> None:
        newTail = ListNode(val)
        newTail.prv = self.tail

        if self.size == 0:
            self.head = newTail # no previous tail
        else:
            self.tail.nxt = newTail
            
        self.tail = newTail

        self.size += 1
        return
    
    def deleteHead(self) -> None:
        # handle edge case
        self.head = self.head.nxt
        self.head.prv = None

        self.size -= 1
        return

    def deleteTail(self) -> None:
        # handle edge case
        self.tail = self.tail.prv
        self.tail.nxt = None
        
        self.size -= 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return # invalid index value
        elif index == 0:
            self.addAtHead(val) # equivalent, handles edge case
            return
        elif index == self.size: 
            self.addAtTail(val) # same reasoning
            return
        
        # guaranteed to be a middle node now
        prv, cur = None, self.head
        i = 0
        while cur != None:
            if i == index:
                newNode = ListNode(val)
                newNode.nxt = cur
                newNode.prv = prv
                prv.nxt = newNode
                cur.prv = newNode
                break
            prv = cur
            cur = cur.nxt
            i += 1
        
        print(newNode.prv.val, newNode.val, newNode.nxt.val)
        self.size += 1
        return

    def deleteAtIndex(self, index: int) -> None:
        print(self.size, index)
        
        if self.size == 0 or index < 0 or index > self.size-1:
            return # invalid index value

        if index == 0:
            self.deleteHead()
            return
        elif index == self.size-1:
            self.deleteTail()
            return

        cur = self.head
        while index > 0:
            cur = cur.nxt
            index -= 1

        cur.prv.nxt, cur.nxt.prv = cur.nxt, cur.prv

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)