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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        wordDict = set(wordDict)
        trie = Trie()

        for word in wordDict:
            trie.add(word)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        
        for i in range(n - 1, -1, -1):
            curr = trie.root
            for j in range(i, n):
                ch = s[j]
                if ch in curr.children:
                    curr = curr.children[ch]
                    if curr.end and dp[j + 1]:
                        dp[i] = True
                else:
                    break

                # if s[i:j + 1] in wordDict:
                #     if dp[j + 1]:
                #         dp[i] = True

        return dp[0]



        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return True
            
            curr = trie.root
            for j in range(i, len(s)):
                ch = s[j]
                if ch in curr.children:
                    curr = curr.children[ch]
                    if curr.end:
                        if dfs(j + 1):
                            memo[i] = True
                            return True
                else:
                    break
                # if s[i:j + 1] in wordDict:
                #     if dfs(j + 1):
                #         memo[i] = True
                #         return True
            
            memo[i] = False
            return False
        
        return dfs(0)