class MagicDictionary:

    def __init__(self):
        self.dict = set()
        

    def buildDict(self, dictionary: list[str]) -> None:
        for word in dictionary:
            self.dict.add(word)
        

    def search(self, searchWord: str) -> bool:

        n = len(searchWord)
        for i in range(n):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if searchWord[i] == ch:
                    continue
                if searchWord[:i] + ch + searchWord[i + 1: ] in self.dict:
                    return True
        return False

        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)