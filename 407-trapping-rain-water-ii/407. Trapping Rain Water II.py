class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        m = len(heightMap)
        n = len(heightMap[0])

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        def valid(r,c):
            return 0<=r<m and 0<=c<n

        boundary = []
        seen = set()
        for i in range(m):
            heapq.heappush(boundary, [heightMap[i][0], i, 0])
            heapq.heappush(boundary, [heightMap[i][n - 1], i, n - 1])
            seen.add((i,0))
            seen.add((i,n - 1))
        
        for i in range(n):
            heapq.heappush(boundary, [heightMap[0][i], 0, i])
            heapq.heappush(boundary, [heightMap[m-1][i], m-1, i])
            seen.add((0,i))
            seen.add((m-1,i))
        
        ans = 0
        while boundary:
            h,r,c = heapq.heappop(boundary)

            min_boundary = h

            for dx, dy in dirs:
                nr,nc = r + dx, c + dy

                if valid(nr,nc) and (nr,nc) not in seen:

                    if heightMap[nr][nc] < min_boundary:
                        ans += min_boundary - heightMap[nr][nc]
                    
                    heapq.heappush(boundary, [max(heightMap[nr][nc], min_boundary), nr, nc])
                    seen.add((nr,nc))
        
        return ans

