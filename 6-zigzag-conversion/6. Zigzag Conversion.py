class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        secs = ceil(n / (2 * numRows - 2.0))
        cols = secs * (numRows - 1)

        i = 0
        matrix = [[" "] * cols for _ in range(numRows)]

        r = 0
        c = 0

        while i < n:

            while i < n and r < numRows:
                matrix[r][c] = s[i]
                r +=1
                i+=1
            
            r -= 2
            c +=1

            while i < n and r > 0 and c < cols:
                matrix[r][c] = s[i]
                r -= 1
                c +=1
                i +=1
        
        ans = ""

        for row in matrix:
            ans+= "".join(row)
        
        return ans.replace(" ","")
