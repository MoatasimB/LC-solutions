class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        n = len(graph)
        if n == 1:
            return 0
        end = (1 << n) - 1
        q = deque()
        seen = set()
        for i in range(n):
            q.append((i, 1 << i, 0))
            seen.add((i,1 << i))
        

        while q:
            node, mask, step = q.popleft()

            if mask == end:
                return step
            
            for nei in graph[node]:
                if (nei, mask | 1 << nei) not in seen:
                    q.append((nei,mask | 1 << nei, step + 1 ))
                    seen.add((nei, mask | 1 << nei))
        