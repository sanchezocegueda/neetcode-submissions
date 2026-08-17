class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def makeWord(self):
        self.isWord = True

class WordDictionary:

    def __init__(self):
        self.root = Node()



    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        
        cur.makeWord()

    def search(self, word: str) -> bool:
        # dfs on the "."s

        return self._helper(self.root, word)


    def _helper(self, node: Node, word: str) -> bool:
        if word == "":
            return node.isWord

        elif node is None:
            return False

        c = word[0]

        if c == '.':
            res = False
            for child in node.children:
                res |= self._helper(node.children[child], word[1:])
                if res:
                    return True
            return False
        else:
            if c not in node.children:
                return False
            return self._helper(node.children[c], word[1:])
