class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        

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
            
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        m = len(board)
        n = len(board[0])

        def valid(r, c):
            return 0<=r<m and 0<=c<n
        
        words = set(words)

        t = Trie()
        for word in words:
            t.add(word)
        
        def dfs(r,c, curr, w, seen):
            if curr.end:
                ans.add(w)

            for dx, dy in dirs:
                nr = dx + r
                nc = dy + c
                
                if valid(nr, nc) and (board[nr][nc] in curr.children) and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    dfs(nr,nc, curr.children[board[nr][nc]], w + board[nr][nc], seen)

                    seen.remove((nr,nc))
        
        # curr = t.root
        ans = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] in t.root.children:
                    seen = set()
                    seen.add((i,j))
                    dfs(i,j,t.root.children[board[i][j]], board[i][j], seen)
        
        return list(ans)
