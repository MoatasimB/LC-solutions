class Node:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word, idx):
        curr = self.root

        for i in range(len(word) - 1, -1, -1):
            ch = word[i]
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
            curr.words.append([word, idx])
    def find(self, suffix):
        curr = self.root

        for ch in reversed(suffix):
            if ch not in curr.children:
                break
            curr = curr.children[ch]
        lst_words = sorted(curr.words, key= lambda x: [len(x[0]), x[1]])
        # print(suffix, curr.words, lst_words)
        return lst_words[0][1] if len(lst_words) != 0 else -1

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        trie = Trie()
        shortest_idx = -1
        shortest_len = float("inf")
        for idx, word in enumerate(wordsContainer):
            trie.add(word, idx)
            if len(word) < shortest_len:
                shortest_len = len(word)
                shortest_idx = idx
        ans = []
        for q in wordsQuery:
            x = trie.find(q)
            if x == -1:
                ans.append(shortest_idx)
            else:
                ans.append(x)
        return ans   