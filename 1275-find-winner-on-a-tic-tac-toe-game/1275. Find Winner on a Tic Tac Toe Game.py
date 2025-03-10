class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        d = 0
        ad = 0

        player = 1

        for i in range(len(moves)):
            r,c = moves[i]

            rows[r] += player
            cols[c] += player

            if r-c == 0:
                d += player
            if r+c == 2:
                ad += player
            
            if abs(rows[r]) == 3 or abs(cols[c]) == 3 or abs(d) == 3 or abs(ad) == 3:
                return "A" if player == 1 else "B"
            
            player *= -1
        
        return "Pending" if len(moves) < 9 else "Draw"