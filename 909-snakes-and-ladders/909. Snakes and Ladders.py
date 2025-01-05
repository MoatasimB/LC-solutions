class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        
        def valid(sq):
            return 1<=sq<=n*n
        
        def isLorS(row,col):
            return board[row][col] != -1
        
        n = len(board)
        seen = {1}
        q = deque([(1,0)])
        
        cell = [None] * (n**2 + 1)
        label = 1
        columns = list(range(0, n))
        for row in range(n - 1, -1, -1):
            for column in columns:
                cell[label] = (row, column)
                label += 1
            columns.reverse()
        
        while q:
            # print(q)
            square, steps = q.popleft()
            
            if square == n*n:
                return steps
            
            # print(square, steps)

            for new_square in range(square + 1, min(square + 6, n**2) + 1):
                new_row, new_col = cell[new_square]
                
                if isLorS(new_row, new_col):
                    next_square = board[new_row][new_col]
                    
                    if next_square not in seen:
                        seen.add(next_square)
                        q.append((next_square, steps+1))
                else:
                    if new_square not in seen:
                        seen.add(new_square)
                        q.append((new_square, steps + 1))

                
#                 if new_square not in seen:
#                     seen.add(new_square)
#                     # q.append((new_row, new_col, new_square, steps + 1))
#                     if isLorS(new_row, new_col):
#                         next_square = board[new_row][new_col]
#                         if next_square == n*n:
#                             return steps + 1

#                         if next_square not in seen:
#                             seen.add(next_square)
#                             q.append((next_square, steps + 1))
#                     else:
#                         # seen.add(new_square)
#                         q.append((new_square, steps + 1))
        return -1 
                    
        
        
        
        
        [
            [-1,-1,-1,46,47,-1,-1,-1],
            [51,-1,-1,63,-1,31,21,-1],
            [-1,-1,26,-1,-1,38,-1,-1],
            [-1,-1,11,-1,14,23,56,57],
            [11,-1,-1,-1,49,36,-1,48],
            [-1,-1,-1,33,56,-1,57,21],
            [-1,-1,-1,-1,-1,-1,2,-1],
            [-1,-1,-1,8,3,-1,6,56]
        ]
        
        
