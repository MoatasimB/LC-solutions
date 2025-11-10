class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)

        ans = 0

        def dfs(node):
            for j in range(n):
                if isConnected[node][j] and j not in seen:
                    seen.add(j)
                    dfs(j)

        seen = set()

        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
        
        return ans


