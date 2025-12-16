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
            


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        dictionary = set(dictionary)
        for word in dictionary:
            trie.add(word)

        memo = {}
        def dfs(i, curr):
            if (i, curr) in memo:
                return memo[(i, curr)]
            if i == len(s):
                return curr
            

            ans = len(s)

            node = trie.root

            for j in range(i, len(s)):
                ch = s[j]
                ans = min(ans, dfs(j + 1, curr + j - i + 1))
                if ch in node.children:
                    node = node.children[ch]
                    if node.end:
                        ans = min(ans, dfs(j + 1, curr))
                else:
                    break



                # if s[i: j + 1] in dictionary:
                #     ans = min(ans, dfs(j + 1, curr))
                # ans = min(ans, dfs(j+1, curr + j - i +1 ))
            memo[(i, curr)] = ans
            return ans
        
        return dfs(0, 0)
