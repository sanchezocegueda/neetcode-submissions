class SegmentTree:

    def __init__(self, start: int, end: int):
        self.left = None
        self.right = None
        self.start = start
        self.end = end

    def insert(self, start: int, end: int) -> bool:
        cur = self
        while True:
            # order should be: end <= cur.start or start <= cur.end to avoid conflicts
            if start >= cur.end:
                if not cur.right: # reached bottom of tree
                    cur.right = SegmentTree(start, end)
                    return True
                cur = cur.right
            elif end <= cur.start:
                if not cur.left:
                    cur.left = SegmentTree(start, end)
                    return True
                cur = cur.left
            else:
                return False
                


class MyCalendar:
    
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = SegmentTree(startTime, endTime)
            return True
        return self.root.insert(startTime, endTime)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)