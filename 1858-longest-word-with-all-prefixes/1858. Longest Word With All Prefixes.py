class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.end = True
    
    def check(self, word):
        curr = self.root
    
        for ch in word:
            if ch not in curr.children:
                
                return False
            curr = curr.children[ch]
            if not curr.end:
                return False
  
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words.sort(key = lambda x: (len(x), x), reverse = True)
        trie = Trie()
        for word in words:
            trie.add(word)
        ans = ""
        curr_len = 0

        for i, word in enumerate(words):
            if len(word) < curr_len:
                break
            if trie.check(word):
                ans = word
                curr_len = len(word)
                # if ans == "aehn":
                #     print("hello")
                # if ans!="" and i + 1 < len(words) and len(words[i + 1]) < len(word):
                #     return ans




        return ans