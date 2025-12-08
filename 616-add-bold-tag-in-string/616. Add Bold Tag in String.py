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
    
    def find(self, s, i) : #find any word in this string s starting from index i
        curr = self.root
        final = -1
        for j in range(i, len(s)):
            ch = s[j]
            if ch in curr.children:
                curr = curr.children[ch]
                if curr.end:
                    final = j
            else:
                break
        return final


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        words = set(words)
        bold = [False] * len(s)
        trie = Trie()

        for word in words:
            trie.add(word)

        for i in range(len(s)):
            end = trie.find(s, i)
            if end != -1:
                for j in range(i, end + 1):
                    bold[j] = True

        # for word in words:
        #     l = 0
        #     r = len(word) - 1

        #     while r < len(s):
        #         if s[l : r + 1] in words:
        #             for i in range(l, r + 1):
        #                 bold[i] = True
        #         l += 1
        #         r += 1
        

        ans = []

        i = 0
        while i < len(s):
            if bold[i]:

                ans.append("<b>")
                while i < len(s) and bold[i]:
                    ans.append(s[i])
                    i += 1
                ans.append("</b>")
            else:
                ans.append(s[i])
                i += 1
        
        return "".join(ans)

