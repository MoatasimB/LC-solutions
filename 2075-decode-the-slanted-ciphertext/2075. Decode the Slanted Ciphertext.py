class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        
        n = len(encodedText)

        cols = n // rows

        grid = [[""] * cols for _ in range(rows)]
        i = 0

        for r in range(rows):
            for c in range(cols):
                grid[r][c] = encodedText[i]
                i += 1
        

        final = []
        def valid(r , c):
            return 0 <= r < rows and 0 <= c < cols
        
        for c in range(cols):
            r = 0
            while valid(r, c):
                final.append(grid[r][c])
                r += 1
                c += 1
        while final and final[-1] == " ":
            final.pop()
        return "".join(final)
