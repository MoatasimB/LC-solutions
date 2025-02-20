class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        def canCrush():
            crushed_set = set()
            #rows
            for r in range(len(board)):
                for c in range(len(board[0]) - 2):
                    if board[r][c] != 0 and board[r][c] == board[r][c+1] == board[r][c + 2]:
                        crushed_set.add((r,c))
                        crushed_set.add((r, c + 1))
                        crushed_set.add((r, c + 2))

            for c in range(len(board[0])):
                for r in range(len(board) - 2):
                    if board[r][c] != 0 and board[r][c] == board[r + 1][c] == board[r + 2][c]:
                        crushed_set.add((r,c))
                        crushed_set.add((r + 1, c))
                        crushed_set.add((r + 2, c))

            for r,c in crushed_set:
                board[r][c] = 0
                #move zeros
            if len(crushed_set) > 0:
                for col in range(len(board[0])):
                    j = len(board) - 1
                    for i in range(len(board)-1, -1, - 1):
                        if board[i][col] != 0:
                            board[i][col], board[j][col] = board[j][col], board[i][col]
                            j -= 1
            
            return len(crushed_set) > 0
        
        while True:
            if not canCrush():
                break



        return board