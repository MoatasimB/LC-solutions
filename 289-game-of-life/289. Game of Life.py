class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        def valid(r,c):
            return 0<=r<m and 0<=c<n

        dirs = [(-1,0), (-1,1), (0,1), (1,1), (1, 0), (1,-1), (0,-1), (-1,-1)]

        def checkN(r,c):
            count = 0

            for dx,dy in dirs:
                newr = r + dx
                newc = c + dy

                if valid(newr, newc) and abs(board[newr][newc]) == 1 :
                    count +=1
            return count
        
    


        for i in range(m):
            for j in range(n):
                val = board[i][j]
                count = checkN(i,j)
                if val == 1 and (count < 2 or count > 3):
                    board[i][j] = -1
                if val == 0 and count == 3:
                    board[i][j] = 2

              
        
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0


