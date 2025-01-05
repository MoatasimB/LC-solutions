class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        def valid(r,c):
            return 0<=r<m and 0<=c<n

        def dfs(r,c):

            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy

                if valid(nr,nc) and board[nr][nc] == 'O':
                    board[nr][nc] = 1
                    dfs(nr,nc)
        

        for r in range(m):
            for c in range(n):
                if (r == 0 or r == m-1 or c==0 or c==n-1) and board[r][c]=='O':
                    board[r][c] = 1
                    dfs(r,c)
        print(board)
        for r in range(m):
            for c in range(n):
                if board[r][c] == 1:
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
