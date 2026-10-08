class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if not endWord in wordList:
            return 0 # early termination

        def editDistance(word1: str, word2: str):
            return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1


        marked = set()

        q = deque()
        q.append((beginWord, 1))

        while q:

            curWord, count = q.popleft()
            # print(curWord, count)

            if curWord in marked:
                continue
            
            if curWord == endWord:
                return count
            

            marked.add(curWord)

            for newWord in wordList:
                if newWord in marked:
                    continue
                

                ed = editDistance(curWord, newWord)
                # print(curWord, newWord, ed)
                if editDistance(curWord, newWord) == 1:
                    q.append((newWord, count+1))
            

        return 0