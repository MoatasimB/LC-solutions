class Node:
    def __init__(self):
        self.children = {}
        self.minLen = float("inf")
        self.idx = -1

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word, idx):
        curr = self.root
        if len(word) < curr.minLen:
            curr.minLen = len(word)
            curr.idx = idx
        for i in range(len(word) - 1, -1, -1):
            ch = word[i]
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
            if len(word) < curr.minLen:
                curr.minLen = len(word)
                curr.idx = idx
    def find(self, suffix):
        curr = self.root

        for ch in reversed(suffix):
            if ch not in curr.children:
                break
            curr = curr.children[ch]
        # print(suffix, curr.words, lst_words)
        return curr.idx
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        trie = Trie()
    
        for idx, word in enumerate(wordsContainer):
            trie.add(word, idx)
            
        ans = []
        for q in wordsQuery:
            x = trie.find(q)
            ans.append(x)
        return ans   