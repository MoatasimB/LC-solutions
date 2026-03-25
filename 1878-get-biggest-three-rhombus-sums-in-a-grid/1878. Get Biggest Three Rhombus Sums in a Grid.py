class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        
        m = len(grid)
        n = len(grid[0])

        def valid(r, c):
            return 0 <= r < m and 0 <= c < n
        
        def checkCorners(r, c, dist):
            return valid(r + dist, c) and valid(r - dist, c) and valid(r, c + dist) and valid(r, c - dist)

        leftPref = [[0] * n for _ in range(m)]
        rightPref = [[0] * n for _ in range(m)]


        for col in range(n):
            r = 0
            c = col
            while valid(r, c):
                rightPref[r][c] = grid[r][c] + (rightPref[r - 1][c - 1] if valid(r - 1, c - 1) else 0)
                r += 1
                c += 1
        
        for row in range(1, m):
            c = 0
            r = row
            while valid(r, c):
                rightPref[r][c] = grid[r][c] + (rightPref[r - 1][c - 1] if valid(r - 1, c - 1) else 0)
                r += 1
                c += 1

        for col in range(n - 1, -1, -1):
            r = 0
            c = col
            while valid(r, c):
                leftPref[r][c] = grid[r][c] + (leftPref[r - 1][c + 1] if valid(r - 1, c + 1) else 0)
                r += 1
                c -= 1
        
        for row in range(1, m):
            c = n - 1
            r = row
            while valid(r, c):
                leftPref[r][c] = grid[r][c] + (leftPref[r - 1][c + 1] if valid(r - 1, c + 1) else 0)
                r += 1
                c -= 1

        final = set()
        
        def getSum(r, c, dist):
            if dist == 0:
                return grid[r][c]
            else:
                
                top = (r - dist, c)
                left = (r, c - dist)
                right = (r, c + dist)
                bottom = (r + dist, c)
                total = 0
                
                #edge top right (l -> r)
                topLR = rightPref[r - dist][c]
                rightLR = rightPref[r][c + dist]
                total += rightLR - topLR + grid[r - dist][c]


                #edge top left (r -> l)
                topRL = leftPref[r - dist][c]
                leftRL = leftPref[r][c - dist]
                total += leftRL - topRL + grid[r - dist][c]


                #edge bottom left
                bottomLR = rightPref[r + dist][c]
                leftLR = rightPref[r][c - dist]
                total += bottomLR - leftLR + grid[r][c - dist]


                #edge bottom right:
                bottomRL = leftPref[r + dist][c]
                rightRL = leftPref[r][c + dist]
                total += bottomRL - rightRL + grid[r][c + dist]

                return total - grid[r + dist][c] - grid[r - dist][c] - grid[r][c + dist] - grid[r][c - dist]



        for r in range(m):
            for c in range(n):
                dist = 0
                while checkCorners(r, c, dist):
                    curr = getSum(r, c, dist)
                    final.add(curr)
                    dist += 1
        
        # print(leftPref)
        # print(rightPref)
        final = sorted(list(final), reverse = True)
        return final[:3]

    

            # [0, 0, 0, 0]
