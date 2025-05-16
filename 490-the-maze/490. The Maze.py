class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        n = len(maze)
        m = len(maze[0])
        
        def valid(r, c):
            return 0<=r<n and 0<=c<m and maze[r][c] != 1

        def move(r,c,dx,dy):
            while valid(r + dx, c +dy):
                r += dx
                c += dy
            return r,c 

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(r, c):
            if [r,c] == destination:
                return True
            seen.add((r,c))
            for dx, dy in dirs:
                nr,nc = move(r,c, dx, dy)
                if valid(nr, nc) and (nr, nc) not in seen:
                    if dfs(nr,nc):
                        return True
            return False
        
        seen = set()
        seen.add((start[0], start[1]))

        return dfs(start[0], start[1])