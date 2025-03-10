class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # if len(moves) == 9:
        #     return "Draw"
        rows = {0: [],
                1 : [], 
                2 : []}
        cols = {0: [],
                1 : [], 
                2 : []}
        
        diagonals = {0 : [], 2: []}

        for i in range(len(moves)):
            r,c = moves[i]
            choice = "X" if i % 2 == 0 else "O"
            rows[r].append(choice)
            cols[c].append(choice)
            if (r-c) == 0:
                diagonals[r-c].append(choice)
            if (r + c) == 2:
                diagonals[r+c].append(choice)
        
        print(rows)
        print(cols)
        print(diagonals)
        for key, val in rows.items():
            if len(val) == 3 and len(set(val)) == 1:
                ans = "A" if val[0] == "X" else "B"
                return ans
        for key, val in cols.items():
            if len(val) == 3 and len(set(val)) == 1:
                ans = "A" if val[0] == "X" else "B"
                return ans
        for key, val in diagonals.items():
            if len(val) == 3 and len(set(val)) == 1:
                ans = "A" if val[0] == "X" else "B"
                return ans
        
        return "Pending" if len(moves) < 9 else "Draw"





        