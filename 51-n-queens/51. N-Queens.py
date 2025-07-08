class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        grid = [["."] * n for _ in range(n)]

        rows = set()
        cols = set()
        pos = set()
        neg = set()
        ans = []
       
        def dfs(r):
            if r == n:
                ans.append(["".join(row) for row in grid])
                return
            
            for c in range(n):
                if r not in rows and c not in cols and (r+c) not in pos and (r-c) not in neg:
                    rows.add(r)
                    cols.add(c)
                    pos.add(r+c)
                    neg.add(r-c)

                    grid[r][c] = "Q"

                    dfs(r+1)

                    grid[r][c] = "."
                    rows.remove(r)
                    cols.remove(c)
                    pos.remove(r+c)
                    neg.remove(r-c)
        

        dfs(0)

        return ans



