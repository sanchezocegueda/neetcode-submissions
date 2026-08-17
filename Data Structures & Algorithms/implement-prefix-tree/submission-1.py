class Node:

    def __init__(self):
        self.isWord = False
        self.children = {}

    def mark(self):
        self.isWord = True

class PrefixTree:

    def __init__(self):
        self.rootNode = Node()

    def insert(self, word: str) -> None:
        cur = self.rootNode
        for c in word:

            if c not in cur.children:
                cur.children[c] = Node()

            cur = cur.children[c]
        
        cur.mark()


    def search(self, word: str) -> bool:
        cur = self.rootNode

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.rootNode

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        