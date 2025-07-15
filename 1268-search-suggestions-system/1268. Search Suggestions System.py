class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        
        class Node:
            def __init__(self):
                self.children = {}
                self.end = False
        
        class Trie:
            def __init__(self):
                self.root = Node()
                self.final = []
            
            def addWord(self, word):
                curr = self.root
                for ch in word:
                    if ch not in curr.children:
                        curr.children[ch] = Node()
                    
                    curr = curr.children[ch]

                curr.end = True
            
            def fw(self, word):
                curr = self.root

                for ch in word:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]
                
                return True
            
            def find(self, pre):
                curr = self.root

                self.final = []
                for ch in pre:
                    if ch not in curr.children:
                        return self.final
                    curr = curr.children[ch]
                
                self.dfs(curr, pre)
                return self.final
            
            def dfs(self, curr, pre):

                if len(self.final) == 3:
                    return
                else:
                    if curr.end:
                        self.final.append(pre)
                    
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch in curr.children:
                            self.dfs(curr.children[ch], pre + ch)

                        
            


        
        t = Trie()

        for word in products:
            t.addWord(word)
        
        ans = []
        for i in range(len(searchWord)):
            ans.append(t.find(searchWord[:i+1]))


        return ans

