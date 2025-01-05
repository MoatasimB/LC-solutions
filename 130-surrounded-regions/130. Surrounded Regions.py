class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        
        def valid(r,c):
            return 0<=r<m and 0<=c<n

        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def dfs(r,c):
            for dx, dy in dirs:
                new_r = r+dx
                new_c = c+dy
                if valid(new_r, new_c) and board[new_r][new_c]=='O':
                    board[new_r][new_c] = 'E'
                    dfs(new_r, new_c)
            
        
        def border(r,c):
            return r==0 or r==m-1 or c==0 or c==n-1
        for i in range(m):
            for j in range(n):
                if border(i,j) and board[i][j] == 'O':
                    board[i][j] = 'E'
                    dfs(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'E':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        




