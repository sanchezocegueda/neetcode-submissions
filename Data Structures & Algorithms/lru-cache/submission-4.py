from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.q = deque()
        self.cap = capacity
        self.cache = {}
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.q.remove(key)
            self.q.append(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.cache[key] = value

            # accessed, so put back at beginning of queue
            self.q.remove(key)
            self.q.append(key)

        else:
            if self.size < self.cap:
                self.cache[key] = value
                self.q.append(key)
                self.size += 1
            else:
                self.cache[key] = value
                self.q.append(key)
                lru = self.q.popleft()
                del self.cache[lru]
        
        return
