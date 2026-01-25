class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        
        #dlru
        m = len(maze)
        n = len(maze[0])
        dir_to_letter = {0: "d", 1: "l", 2: "r", 3: "u"}
    
        
        def valid(r, c):
            return 0 <= r < m and 0 <= c < n and maze[r][c] == 0
        
        dirs = [(1, 0), (0, -1), (0,1), (-1, 0)]

        def nextPos(currR, currC, direction):
            dx, dy = direction
            dist = 0
            while valid(currR + dx, currC + dy):
                currR = currR + dx
                currC = currC + dy
                dist += 1
                if [currR, currC] == hole:
                    break
            
            return [currR, currC, dist]
        
        dists = [[float("inf")] * n for _ in range(m)]
        minHeap = [[0, "", ball[0], ball[1]]]

        dists[ball[0]][ball[1]] = 0
        #r, c, path, cost
        min_cost = float("inf")
        seen = set()
        while minHeap:
            cost, path, r, c = heapq.heappop(minHeap)
            if (r, c) in seen:
                continue 

            if [r, c] == hole:
                return path
            
            seen.add((r, c))
            for i, direction in enumerate(dirs):

                nr, nc, dist = nextPos(r, c, direction)

                if (nr, nc) not in seen:
                    heapq.heappush(minHeap, [cost + dist, path + dir_to_letter[i], nr, nc ])

    
        
        return "impossible"
        
      

