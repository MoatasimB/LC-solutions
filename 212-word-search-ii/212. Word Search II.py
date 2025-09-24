class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        m = len(board)
        n = len(board[0])
        class Node:
            def __init__(self):
                self.children = [None] * 26
                self.end = False
                self.word = None
        
        class Trie:
            def __init__(self):
                self.root = Node()
            
            def add(self, word):
                curr = self.root
                
                for ch in word:
                    if not curr.children[ord(ch) - ord('a')]:
                        curr.children[ord(ch) - ord('a')] = Node()
                    
                    curr = curr.children[ord(ch) - ord('a')]
                
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
                
                if valid(nr,nc) and (nr,nc) not in seen and currNode.children[ord(board[nr][nc]) - ord('a')]:
                    seen.add((nr,nc))
                    dfs(nr,nc,currNode.children[ord(board[nr][nc]) - ord('a')],seen)
                    seen.remove((nr,nc))
        
        currNode = trie.root
        ans = []
        for r in range(m):
            for c in range(n):
                if currNode.children[ord(board[r][c]) - ord('a')]:
                    dfs(r, c, currNode.children[ord(board[r][c]) - ord('a')], set([(r,c)]))
        
        
        return list(set(ans))
                
                    
            