class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        adj = defaultdict(list)
        n = len(isConnected)
        
        for i in range(n):
            for j in range(i):
                if isConnected[i][j]:
                    adj[i].append(j)
                    adj[j].append(i)
        
        print(adj)
        def dfs(node):
            for i in range(len(isConnected[node])):
                if isConnected[node][i] and i not in seen:
                    seen.add(i)
                    dfs(i)
        p = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                p += 1
        
        return p