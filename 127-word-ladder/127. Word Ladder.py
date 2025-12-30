class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        def getNeighbors(word):
            neighbors = []

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in wordList:
                        neighbors.append(new_word)
            return neighbors
        

        q = deque()
        seen = set()
        q.append([beginWord, 1])
        seen.add(beginWord)

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps
            
            for nei in getNeighbors(word):
                if nei not in seen:
                    seen.add(nei)
                    q.append([nei, steps + 1])
        
        return 0