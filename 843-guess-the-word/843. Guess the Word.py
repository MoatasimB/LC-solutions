# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:

        def getMatches(word1, word2):
            count = 0
            for c1, c2 in zip(word1, word2):
                if c1 == c2:
                    count += 1
            return count
        
        candidates = words

        for i in range(30):

            #check
            idx = random.randint(0, len(candidates) - 1)
            w1 = candidates[idx]
            c = master.guess(w1)
            if c == 6:
                break
            new = []
            for word in candidates:
                matches = getMatches(w1, word)
                if matches == c:
                    new.append(word)
            candidates = new
        




        # X X X X z z

        # c c b a z z = 3

        # e i o w z z = 2 #last 2 must be zz and first 4 must contain c b or a
        # a b c c z z = 4