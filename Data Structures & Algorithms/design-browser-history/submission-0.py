class HistoryNode:
    def __init__(self, url: str):
        self.url = url
        self.prv = None
        self.nxt = None

class BrowserHistory:

    def __init__(self, homepage: str):
        home = HistoryNode(homepage)
        self.head = home

    def visit(self, url: str) -> None:
        newVisit = HistoryNode(url)
        newVisit.prv = self.head
        self.head.nxt = newVisit
        self.head = newVisit

    def back(self, steps: int) -> str:
        
        prv = None # in case we overflow
        while self.head != None and steps > 0:
            prv = self.head # last position head was in
            self.head = self.head.prv
            steps -= 1
        
        if self.head is None:
            self.head = prv
        return self.head.url

    def forward(self, steps: int) -> str:
        
        prv = None # in case we overflow
        while self.head != None and steps > 0:
            prv = self.head
            self.head = self.head.nxt
            steps -= 1
        
        if self.head is None:
            self.head = prv
        return self.head.url




# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)