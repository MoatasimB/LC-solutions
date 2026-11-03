class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])
        rows = defaultdict(int)
        cols = defaultdict(int)
        cells = []
        for r in range(m):
            for c in range(n):
                if picture[r][c] == "B":
                    cells.append((r, c))
                    rows[r] += 1
                    cols[c] += 1
                
        ans = 0
        for r, c in cells:
            if rows[r] == 1 and cols[c] == 1:
                ans += 1
        
        return ans
