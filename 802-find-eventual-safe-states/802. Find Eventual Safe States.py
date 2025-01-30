class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        inDeg = [0] * len(graph)
        adj = defaultdict(list)
        for i in range(len(graph)):
                inDeg[i] += len(graph[i])
                for j in graph[i]:
                    adj[j].append(i)
        
        q = deque()

        for i in range(len(inDeg)):
            if inDeg[i] == 0:
                q.append(i)

        ans = [False] * len(graph)
        while q:

            node = q.popleft()

            ans[node] = True

            for nei in adj[node]:
                inDeg[nei] -= 1
                if inDeg[nei] == 0:
                    q.append(nei)
        
        final = []

        for i in range(len(ans)):
            if ans[i]:
                final.append(i)
        return final