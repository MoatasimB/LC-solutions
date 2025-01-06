class Node:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = Node()


    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root

        def dfs(word, currentNode):
            curr = currentNode
            for i in range(len(word)):
                if word[i] == '.':
                    for child in curr.children:
                        if dfs(word[i+1:], curr.children[child]):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    
                    curr = curr.children[word[i]]

            return curr.end
        return dfs(word, curr)
                    





# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)