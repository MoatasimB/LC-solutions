class Node:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.head = Node()
    
    def add(self, word):
        curr = self.head

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.end = True

class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        

        stack = []
        n = len(s)
        trie = Trie()
        for word in words:
            trie.add(word)
        
        for i, ch in enumerate(s):
            if ch in trie.head.children:
                j = i
                curr = trie.head
                while j < n and s[j] in curr.children:
                    curr = curr.children[s[j]]
                    if curr.end:
                        stack.append([i, j + 1])
                    j += 1
        if not stack:
            return s
        #merge intervals
        m = len(stack)
        print(stack)
        final = [stack[0]]
        for i in range(1, m):
            start, end = stack[i]
            prevS, prevEnd = final[-1]

            if start <= prevEnd:
                final[-1][1] = max(end, prevEnd)
            else:
                final.append([start, end])
        
        print(final)
        ans = []
        j = 0
        i = 0
        while i < n:
            if j < len(final):
                posStart, posEnd = final[j]
                while i < n and i < posStart:
                    ans.append(s[i])
                    i += 1
                ans.append("<b>")
                while i < n and i < posEnd:
                    ans.append(s[i])
                    i += 1
                ans.append("</b>")
                j += 1
            else:
                ans.append(s[i])
                i += 1
        
        return "".join(ans)



