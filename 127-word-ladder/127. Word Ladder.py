class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        
        mpp = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                mpp[word[:i] + "*" + word[i + 1:]].append(word)
        
        
        
        q = deque()
        seen = set()
        q.append([beginWord, 1])
        seen.add(beginWord)

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for nei in mpp[word[:i] + "*" + word[i + 1:]]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append([nei, steps + 1])
        
        return 0