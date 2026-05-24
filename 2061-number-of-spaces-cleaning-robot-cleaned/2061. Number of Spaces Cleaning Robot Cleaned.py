class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        
        m = len(room)
        n = len(room[0])
        def valid(r, c):
            return 0 <= r < m and 0 <= c < n and room[r][c] != 1
        orientation = [(0,1), (1,0), (0,-1), (-1,0)]
        seen = set()
        clean = set()
        def dfs(r, c, d):
            # print(r, c, d)
            clean.add((r, c))
            seen.add((r, c, d))
            
            for i in range(4):
                dx, dy = orientation[(i + d) % 4]
                nr, nc = r + dx, c + dy
                if valid(nr, nc):
                    if (nr, nc, (i + d) % 4) in seen:
                        return False
                    if not dfs(nr, nc, (i + d) % 4):
                        return False



            return False
        
        dfs(0, 0, 0)
        # print(clean)
        return len(clean)

        [
            [0,0,0],
            [0,0,1]
            ]

        # r, c, d = 0,0,0
        # seen = set()
        # clean = set()
        # while (r, c, d) not in seen:
        #     seen.add((r, c, d))
        #     clean.add((r, c))

        #     dx, dy = orientation[d]
        #     while valid(r + dx, c + dy):
        #         r += dx
        #         c += dy
        #         seen.add((r, c, d))
        #         clean.add((r, c))
            
        #     #next d
        #     r -= dx
        #     c -= dy


