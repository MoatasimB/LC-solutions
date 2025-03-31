class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ans = [0] * len(queries)
        m = len(grid)
        n = len(grid[0])

        queries = [[val, idx] for idx, val in enumerate(queries)]
        queries.sort()
        def valid(r,c):
            return 0<=r<m and 0<=c<n
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        seen = set()
        
        min_heap = [[grid[0][0], 0,0]]
        seen.add((0,0))
        count = 0
        for query,idx in queries:
            # print(query)
            while min_heap and min_heap[0][0] < query:
                val, r,c = heappop(min_heap)
                count += 1
                # if val < query:
                #     count += 1
                # else:
                #     break
                for dx, dy in dirs:
                    nr, nc = r + dx, c + dy
                    if valid(nr,nc) and (nr,nc) not in seen:
                        seen.add((nr,nc))
                        heapq.heappush(min_heap,[grid[nr][nc], nr, nc])
            ans[idx] = count
        
        return ans