class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        def conversion(square):
            
            row = (square - 1) // n
            
            col = (square - 1) % n
            
            if n % 2 == 0:
                if (n-row-1) % 2 == 0:
                    col = n - 1 - col
            else:
                if (n-row-1) % 2 != 0:
                    col = n - 1 - col
                
            
            return [n-row -1, col]
                
            
   


        n = len(board)
        
        seen = {1}
        q = deque([(1, 0)])
        
        while q:
            
            square, steps = q.popleft()
            
            if square == n**2:
                print(square, steps)
                return steps
            
            for next_square in range(square + 1, min(square + 6, n**2) + 1):
                row, col = conversion(next_square)
                
                print(row, col, next_square)
                if board[row][col] != -1:
                    if board[row][col] not in seen:
                        seen.add(board[row][col])
                        q.append((board[row][col], steps + 1))
                else:
                    if next_square not in seen:
                        seen.add(next_square)
                        q.append((next_square, steps + 1))
            
        
        return -1
                
                