class Node:
    def __init__(self):
        self.children = {}
        self.val = 0

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word, val):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
            curr.val += val
    
    def find(self, pref):
        curr = self.root

        for ch in pref:
            if ch not in curr.children:
                return 0
            curr = curr.children[ch]
        
        return curr.val

class MapSum:

    def __init__(self):
        self.words = {} #word : val
        self.trie = Trie()
        

    def insert(self, key: str, val: int) -> None:
        diff = val
        if key in self.words:
            diff = val - self.words[key]
        
        self.words[key] = val
        self.trie.add(key, diff)
        

    def sum(self, prefix: str) -> int:
        return self.trie.find(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)