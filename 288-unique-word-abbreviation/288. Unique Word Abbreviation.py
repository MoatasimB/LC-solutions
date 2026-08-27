class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.mpp = defaultdict(set) #key : set
        for word in dictionary:
            key = self.makeKey(word)
            self.mpp[key].add(word)

    def makeKey(self, word):
        word_len = len(word)
        if word_len == 2:
            return word
        else:
            return word[0] + str(word_len - 2) + word[word_len - 1]

    def isUnique(self, word: str) -> bool:
        key = self.makeKey(word)
        if key not in self.mpp:
            return True
        
        if word in self.mpp[key] and len(self.mpp[key]) == 1:
            return True
        
        return False
        
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)