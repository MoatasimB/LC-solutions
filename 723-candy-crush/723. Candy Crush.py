class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        def crush():

            crushed = set()

            for r in range(len(board) - 2):
                for c in range(len(board[0])):
                    if board[r][c] != 0 and board[r][c] == board[r + 1][c] == board[r+2][c]:
                        crushed.add((r,c))
                        crushed.add((r+1, c))
                        crushed.add((r+2, c))
            for r in range(len(board)):
                for c in range(len(board[0]) - 2):
                    if board[r][c] != 0 and board[r][c] == board[r][c + 1] == board[r][c + 2]:
                        crushed.add((r, c))
                        crushed.add((r, c + 1))
                        crushed.add((r, c + 2))
            
            if len(crushed) > 0:
                for r,c in crushed:
                    board[r][c] = 0
            

                for c in range(len(board[0])):
                    last = len(board) - 1
                    for r in range(len(board) - 1, -1, -1):
                        if board[r][c] != 0:
                            board[r][c], board[last][c] = board[last][c], board[r][c]
                            last -= 1
            
            return crushed

        while len(crush()) > 0:
            crush()

                        

        return board