class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m = len(board)
        n = len(board[0])

        def crush():
            cells_to_crush = set()
            #column
            for col in range(n):
                for row in range(1, m - 1):
                    prev = board[row - 1][col]
                    curr = board[row][col]
                    next = board[row + 1][col]

                    if prev == curr == next and curr != 0:
                        cells_to_crush.add((row - 1, col))
                        cells_to_crush.add((row, col))
                        cells_to_crush.add((row + 1, col))


            #row
            for row in range(m):
                for col in range(1, n - 1):
                    prev = board[row][col - 1]
                    curr = board[row][col]
                    next = board[row][col + 1]

                    if prev == curr == next and curr != 0:
                        cells_to_crush.add((row, col - 1))
                        cells_to_crush.add((row, col))
                        cells_to_crush.add((row, col + 1))
            for r, c in cells_to_crush:
                board[r][c] = 0
            
            print(board)
            return len(cells_to_crush) > 0
        
        def moveDown():
            for col in range(n):
                i = m

                for row in range(m - 1, -1, -1):
                    if board[row][col] == 0:
                        continue
                    else:
                        board[row][col], board[i - 1][col] = board[i - 1][col], board[row][col]
                        i -= 1
        
        while True:
            if not crush():
                break
            moveDown()
        
        return board

       