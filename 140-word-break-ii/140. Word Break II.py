class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = None

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
        curr.word = word

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        
        wordDict = set(wordDict)
        trie = Trie()
        for word in wordDict:
            trie.add(word)
        ans = []
        def dfs(i, curr):
            if i == len(s):
                ans.append(" ".join(curr[:]))
                return
            node = trie.root
            for j in range(i, len(s)):
                ch = s[j]
                if ch in node.children:
                    node = node.children[ch]
                    if node.end:
                        curr.append(node.word)
                        dfs(j + 1, curr)
                        curr.pop()
                else:
                    break



                # word = s[i:j + 1]
                # if word in wordDict:
                #     curr.append(word)
                #     dfs(j + 1, curr)
                #     curr.pop()
        

        dfs(0, [])
        return ans
            