class Solution:
    def totalNQueens(self, n: int) -> int:
        
        cols = set()
        posD = set()
        negD = set()

        ans = 0
        def dfs(r):
            nonlocal ans
            if r == n:
                ans += 1
            
            for col in range(n):
                if (col not in cols) and (r + col not in posD) and (r - col not in negD):
                    cols.add(col)
                    posD.add(r+col)
                    negD.add(r-col)

                    dfs(r+1)

                    cols.remove(col)
                    posD.remove(r+col)
                    negD.remove(r-col)
        
        dfs(0)
        return ans