class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        
        grid = [[False] * 3 for _ in range(3)]

        graph = {
            1: [2, 4, 5, 6, 8],
            2: [1, 3, 4, 5, 6, 7, 9],
            3: [2, 5, 6, 4, 8],
            4: [1, 2, 5, 7, 8, 3, 9],
            5: [1, 2, 3, 4, 6, 7, 8, 9],
            6: [2, 3, 5, 8, 9, 1, 7],
            7: [4, 5, 6, 8, 2],
            8: [4, 5, 6, 7, 9, 1, 3],
            9: [5, 6, 8, 2, 4],
        }



        # def valid(r, c):
        #     return 0<=r<3 and 0<=c<3
        
        # dirs = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

        def dfs(node, pathLen):
            count = 0
            if m <= pathLen <= n:
                count += 1
            if pathLen == n:
                return count
            for nei in range(1, 10):
                if nei == node:
                    continue
                
                if nei not in seen and pathLen < n and (nei in graph[node] or (nei + node) // 2 in seen):
                    seen.add(nei)
                    count += dfs(nei, pathLen + 1)
                    seen.remove(nei)
            
            return count

        
        # def dfs(r, c, pathLen):
            # count = 0
            # if m <= pathLen <= n:
            #     count += 1
            # if pathLen == n:
            #     return count
            # for dx, dy in dirs:
            #     nr = r + dx
            #     nc = c + dy

            #     if valid(nr,nc) and not grid[nr][nc] and pathLen < n:
            #         grid[nr][nc] = True
            #         count += dfs(nr, nc, pathLen + 1)
            #         grid[nr][nc] = False
            
            # return count
        
        ans = 0
        # for r in range(3):
            # for c in range(3):
            #     grid[r][c] = True
            #     ans += dfs(r, c, 1)
            #     grid[r][c] = False
        seen = set()
        for i in range(1, 10):
            seen.add(i)
            ans += dfs(i, 1)
            seen.remove(i)
        return ans