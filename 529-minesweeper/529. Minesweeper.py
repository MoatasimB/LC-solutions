class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        
        cells_adj_bomb = defaultdict(int)

        rows = len(board)
        cols = len(board[0])

        def valid(r,c):
            return 0<=r<rows and 0<=c<cols

        q = []
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "M":
                    q.append((r,c))
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

        for r,c in q:
            for dx, dy in dirs:
                cells_adj_bomb[r+dx, c+dy] += 1
        


        # if (click[0], click[1]) in cells_adj_bomb:
        #     board[click[0]][click[1]] = str(cells_adj_bomb[click[0], click[1]])
        #     return board
        

        q = deque()
        q.append((click[0], click[1]))
        seen = set((click[0], click[1]))

        while q:
            r, c = q.popleft()
            
            if (r,c) in cells_adj_bomb:
                board[r][c] = str(cells_adj_bomb[(r,c)])
                continue
            
            board[r][c] = "B"

            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy
                if valid(nr,nc) and (nr,nc) not in seen:
                    q.append((nr,nc))
                    seen.add((nr,nc))
        
        return board
