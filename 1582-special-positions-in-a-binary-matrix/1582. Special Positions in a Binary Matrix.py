class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        m = len(mat)
        n = len(mat[0])
        rows = defaultdict(int)
        cols = defaultdict(int)
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
        
        ans = 0

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1 and rows[r] == 1 and cols[c] == 1:
                    ans += 1
        
        return ans