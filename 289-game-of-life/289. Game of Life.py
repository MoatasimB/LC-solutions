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

                if valid(newr, newc) and copy[newr][newc] == 1:
                    count +=1
            return count
        
        copy = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                copy[i][j] = board[i][j]


        for i in range(m):
            for j in range(n):
                val = copy[i][j]
                count = checkN(i,j)
                if val == 0 and count == 3:
                    board[i][j] = 1
                elif val == 1 and (count < 2 or count > 3):
                    board[i][j] = 0
                # elif val == 1 and count > 3:
                #     board[i][j] == 0
                # elif val == 1 and count == 2 or count == 3:
                #     board[i][j] == 1
        



