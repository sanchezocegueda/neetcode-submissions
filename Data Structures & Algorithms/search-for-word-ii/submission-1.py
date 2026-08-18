class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def mark(self):
        self.isWord = True
    

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.mark()
        return

    def startsWith(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord


        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # use a trie
        # dfs to add?
        # i don't think we can add all of them, can we?

        trie = PrefixTree()

        for word in words:
            trie.insert(word)
        
        marked = set()
        found = set()

        m, n = len(board), len(board[0])

        def dfs(i, j, curWord, curNode, m, n):

            if (i, j) in marked:
                return
            
            marked.add((i, j))
            c = board[i][j]
            newWord = curWord + c
            newNode = None


            if c in curNode.children:
                if curNode.children[c].isWord:
                    found.add(newWord)
                newNode = curNode.children[c]


            if newNode:

                for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    in_bounds = (0 <= ii < m) and (0 <= jj < n)

                    if in_bounds and (ii, jj) not in marked:
                        dfs(ii, jj, newWord, newNode, m, n)
            
            marked.remove((i, j))

        for i in range(m):
            for j in range(n):
                dfs(i, j, "", trie.root, m, n)


        return list(found)



