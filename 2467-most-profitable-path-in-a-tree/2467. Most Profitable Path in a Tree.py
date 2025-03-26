class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # times = [0] * len(amount)
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        def bfs(node):
            q = deque()
            seen = set()
            q.append((node))
            seen.add(node)
            path = {node:node}
            while q:
                node = q.popleft()

                if node == 0:
                    curr = node
                    final = []
                    while path[curr] != curr:
                        final.append(curr)
                        curr = path[curr]
                    
                    final.append(bob)
                    return final[::-1]
                
                for nei in adj[node]:
                    if nei not in seen:
                        seen.add(nei)
                        path[nei] = node
                        q.append((nei))
            
        final = bfs(bob)
        # print(final)
        times = [float('inf')] * len(amount)
        for i in range(len(final)):
            times[final[i]] = i

        seen = set()
        seen.add(0)
        print(times)
        ret = float('-inf')
        def dfs(node, time, curr):
            nonlocal ret
            bobsTime = times[node]
            ans = 0
            if time < bobsTime:
                ans += amount[node]
            elif time == bobsTime:
                ans += amount[node] // 2
            
            if len(adj[node]) == 1 and node != 0:
                print(f"leaf node = {node} returning: {ans}")
                ret = max(ret, ans + curr)
                return
            
            for nei in adj[node]:
                if nei not in seen:
                    seen.add(node)
                    dfs(nei, time + 1, ans + curr)

        
        dfs(0, 0, 0)
        return ret
        
                    
                
            
