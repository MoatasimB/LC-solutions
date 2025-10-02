class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def valid(row,col):
            return 0<=row<m and 0<=col<n
        
        
        def fireTime():

            fireGrid = [[float("inf")] * n for _ in range(m)]
            q = deque()

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        q.append((i,j,0))

            while q:
                row,col,time = q.popleft()

                if fireGrid[row][col] <= time:
                    continue
                
                fireGrid[row][col] = time

                for dx,dy in directions:
                    next_row = row+dx
                    next_col = col+dy

                    if valid(next_row,next_col) and grid[next_row][next_col] !=2:
                        q.append((next_row,next_col, time + 1))
            
            return fireGrid

        
        def check(mid,fireGrid):

            reachGrid = [[float("inf")] * n for _ in range(m)]
            q = deque()

  
            q.append((0,0,mid))

            while q:
                row,col,time = q.popleft()

                if (row,col) == (m-1, n-1) and time <= fireGrid[row][col]:
                    return True

                if reachGrid[row][col] <= time or time>=fireGrid[row][col]:
                    continue
                
                reachGrid[row][col] = time

                for dx,dy in directions:
                    next_row = row+dx
                    next_col = col+dy

                    if valid(next_row,next_col) and grid[next_row][next_col] !=2:
                        q.append((next_row,next_col, time + 1))
            
            return False
        
        fireGrid = fireTime()
        left = 1
        right = 1000000000

        if not check(0,fireGrid):
            return -1
        
        if check(float("inf"),fireGrid):
            return 10**9


        while left<= right:
            mid = (left + right)//2

            if check(mid,fireGrid):
                left = mid + 1
            else:
                right = mid - 1
        
        return right
