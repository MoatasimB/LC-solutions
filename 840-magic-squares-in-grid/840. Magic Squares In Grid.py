class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def check(startR, startC):
            seen = set()
            rows = defaultdict(int)
            cols = defaultdict(int)
            pos_diag = 0
            neg_diag = 0
            for r in range(startR, startR + 3):
                for c in range(startC, startC + 3):
                    if grid[r][c] in seen or not (1 <= grid[r][c] <= 9):
                        return False
                    val = grid[r][c]
                    seen.add(val)

                    rows[r - startR] += val
                    cols[c - startC] += val
                    if r - c == startR - startC:
                        neg_diag += val
                    if r + c == startR + startC + 2:
                        pos_diag += val
            # if (startR, startC) == (1,0):
            #     print(pos_diag, neg_diag)
            #     print(rows, cols)
            if pos_diag != neg_diag:
                return False
            for i in range(3):
                
                r_sum = rows[i]
                c_sum = cols[i]
                # if (startR, startC) == (1, 0):
                #     print(i, r_sum, c_sum)
                if r_sum != pos_diag or c_sum != pos_diag:
                    return False
            return len(seen) == 9
        
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for r in range(m - 2):
            for c in range(n - 2):
                if check(r, c):
                    ans += 1
        
        return ans

# [
#     [3,2,9,2,7],
#     [6,1,8,4,2],
#     [7,5,3,2,7],
#     [2,9,4,9,6],
#     [4,3,8,2,5]]

#             (2, 3) (2, 4) (2, 5)
#             (3, 3) (3, 4) (3, 5)
#             (4, 3) (4, 4) (4, 5)