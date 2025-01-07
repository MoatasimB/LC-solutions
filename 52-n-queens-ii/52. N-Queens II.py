class Solution:
    def totalNQueens(self, n: int) -> int:
        
        COLS = set()
        PD = set()
        ND = set()

        def backtrack(r):

            if r == n:
                return 1
            
            sols = 0

            for c in range(n):
                if c not in COLS and (r-c) not in ND and (r+c) not in PD:

                    COLS.add(c)
                    PD.add(r+c)
                    ND.add(r-c)

                    sols += backtrack(r+1)

                    COLS.remove(c)
                    PD.remove(r+c)
                    ND.remove(r-c)
            
            return sols
        return backtrack(0)

