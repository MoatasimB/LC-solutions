class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        def neighbors(word):
            ans = []
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new = word[:i] + ch + word[i+1:]
                    if new in wordList:
                        ans.append(new)
            return ans
            
        q = deque()

        seen = set()

        q.append((beginWord, 0))
        seen.add(beginWord)

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps + 1
            

            for nei in neighbors(word):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, steps + 1))
        
        return 0
