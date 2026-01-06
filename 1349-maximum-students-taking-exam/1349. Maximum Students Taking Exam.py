class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        
        m = len(seats)
        n = len(seats[0])

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n
        
        def canPlace(r, c, prevRow, currRow):
            dirs = [(0, 1), (0,-1), (-1, -1), (-1, 1)]
            left = c > 0 and currRow & 1 << (c - 1)
            right = c + 1 < n and currRow & 1 << (c + 1)
            topLeft = r > 0 and c > 0 and prevRow & 1 << (c - 1)
            topRight = r > 0 and c + 1 < n and prevRow & 1 << (c + 1)

            if not (left or right or topLeft or topRight):
                return True
            return False
            # for dx, dy in dirs:
            #     nr = r + dx
            #     nc = c + dy
            #     if valid(nr, nc) and seats[nr][nc] == "1":
            #         return False
            # return True


        memo = {}
        def dfs(r, c, prevRow, currRow):
            if (r, c, prevRow, currRow) in memo:
                return memo[(r, c, prevRow, currRow)]
            if r == m:
                return 0

            ans = float("-inf")
            #place
            nr = r if c != n - 1 else r + 1
            nc = c + 1 if c != n - 1 else 0
            if c == 0:
                prevRow = currRow
                currRow = 0
            if seats[r][c] == "." and canPlace(r, c, prevRow, currRow):

                seats[r][c] = "1"
                currRow ^= 1 << c

                ans = max(ans, 1 + dfs(nr, nc, prevRow, currRow))
                seats[r][c] = "."
                currRow ^= 1 << c
            
            #dont place

            ans = max(ans, dfs(nr, nc, prevRow, currRow))
            memo[(r, c,prevRow, currRow)] = ans
            return ans
        
        return dfs(0, 0, 0, 0)



