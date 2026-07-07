class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.words = set(dictionary)
        self.mpp = defaultdict(set)
        for word in dictionary:
            abbrev = self.makeAbbrev(word)
            self.mpp[abbrev].add(word)
        print(self.words)
    def isUnique(self, word: str) -> bool:
        wordAbbrev = self.makeAbbrev(word)
        if wordAbbrev not in self.mpp:
            return True
        if wordAbbrev in self.mpp:
            if len(self.mpp[wordAbbrev]) > 1 or word not in self.mpp[wordAbbrev]:
                return False
            return True
        

        # return self.makeAbbrev(word) not in self.abbreviations or word in self.words
    def makeAbbrev(self, word):
        if len(word) == 2:
            return word
        
        middle = len(word) - 2

        return word[0] + str(middle) + word[-1]



# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)