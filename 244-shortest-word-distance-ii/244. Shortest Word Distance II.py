class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordIndices = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.wordIndices[word].append(i)

        

    def shortest(self, word1: str, word2: str) -> int:
        w1 = self.wordIndices[word1]
        w2 = self.wordIndices[word2]
        n = len(w1)
        m = len(w2)
        i = 0
        j = 0
        ans = float("inf")

        while i < n and j < m:
            ans = min(ans, abs(w1[i] - w2[j]))
            if w1[i] < w2[j]:
                i += 1
            else:
                j += 1
        return ans        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)