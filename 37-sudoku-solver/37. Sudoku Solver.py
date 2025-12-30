class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        row_mpp = defaultdict(set)
        col_mpp = defaultdict(set)
        box_mpp = defaultdict(set)

        m = len(board)
        n = len(board[0])

        for r in range(m):
            for c in range(n):
                val = board[r][c]
                if val == '.':
                    continue
                row_mpp[r].add(val)
                col_mpp[c].add(val)
                box_mpp[(r//3, c//3)].add(val)
        

        def dfs(r, c):
            if r == m:
                return True
            
            if board[r][c] == ".":
                for val in "123456789":
                    if val not in row_mpp[r] and val not in col_mpp[c] and val not in box_mpp[(r//3, c//3)]:
                        
                        board[r][c] = val
                        
                        row_mpp[r].add(val)
                        col_mpp[c].add(val)
                        box_mpp[(r//3, c//3)].add(val)

                        if c == n - 1:
                            if dfs(r + 1, 0):
                                return True
                        else:
                            if dfs(r, c + 1):
                                return True

                        board[r][c] = '.' 
                        row_mpp[r].remove(val)
                        col_mpp[c].remove(val)
                        box_mpp[(r//3, c//3)].remove(val)

            elif c == n - 1:
                if dfs(r + 1, 0):
                    return True
            else:
                if dfs(r, c + 1):
                    return True
        
        dfs(0,0)
            
                        


    


