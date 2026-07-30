class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    
    def __init__(self, capacity: int):
        self.table = [[] for _ in range(capacity)]
        self.cap = capacity
        self.size = 0

    def insert(self, key: int, value: int) -> None:
        h = hash(key) % self.cap

        for x in self.table[h]:
            if x.key == key:
                x.val = value
                return # update element and return
        
        # new element inserted
        x = Node(key, value)
        self.table[h].append(x)
        self.size += 1
        if self.size / self.cap >= 0.5:
            self.resize()


    def get(self, key: int) -> int:
        h = hash(key) % self.cap
        
        for x in self.table[h]:
            if x.key == key:
                return x.val
        
        return -1



    def remove(self, key: int) -> bool:
        h = hash(key) % self.cap

        for i, x in enumerate(self.table[h]):
            if x.key == key:
                self.table[h].pop(i)
                self.size -= 1
                return True
        
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        self.cap *= 2
        newTable = [[] for _ in range(self.cap)]
        
        for lst in self.table:
            for x in lst:
                h = hash(x.key) % self.cap
                newTable[h].append(x)

        self.table = newTable
        return

