class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        m = len(board)
        n = len(board[0])
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
            
        
        trie = Trie()
        
        for word in words:
            trie.add(word)
        
        
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def valid(r,c):
            return 0<=r<m and 0<=c<n
        
        
        def dfs(r, c, currNode, seen):
            if currNode.end:
                ans.append(currNode.word)
            
            for dx, dy in dirs:
                nr, nc = r + dx, c + dy
                
                if valid(nr,nc) and (nr,nc) not in seen and board[nr][nc] in currNode.children:
                    seen.add((nr,nc))
                    dfs(nr,nc,currNode.children[board[nr][nc]],seen)
                    seen.remove((nr,nc))
        
        currNode = trie.root
        ans = []
        for r in range(m):
            for c in range(n):
                if board[r][c] in currNode.children:
                    dfs(r, c, currNode.children[board[r][c]], set([(r,c)]))
        
        
        return list(set(ans))
                
                    
            